import java.math.BigDecimal;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

public class Bank {

    private static final String DORMANT_PREFIX = "D-";

    // Thread-safe map for account storage
    private final Map<String, Account> accounts = new ConcurrentHashMap<>();

    /** Creates a new account with an initial balance (double convenience overload). */
    public void addAccount(String accountId, String accountHolder, double initialBalance) {
        addAccount(accountId, accountHolder, BigDecimal.valueOf(initialBalance));
    }

    /** Creates a new account with an initial balance. */
    public void addAccount(String accountId, String accountHolder, BigDecimal initialBalance) {
        validateAccountId(accountId);
        Objects.requireNonNull(accountHolder, "accountHolder must not be null");
        Objects.requireNonNull(initialBalance, "initialBalance must not be null");
        if (initialBalance.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Initial balance must be non-negative");
        }

        Account newAccount = new Account(accountId, accountHolder, initialBalance);
        Account existing = accounts.putIfAbsent(accountId, newAccount);
        if (existing != null) {
            throw new IllegalArgumentException("Account with id " + accountId + " already exists");
        }
    }

    /** Looks up an account if it exists and is not considered dormant. */
    public Optional<Account> findAccount(String accountId) {
        validateAccountId(accountId);
        if (isDormantAccountId(accountId)) {
            return Optional.empty();
        }
        return Optional.ofNullable(accounts.get(accountId));
    }

    /** Internal helper to get a non-dormant, existing account or fail fast. */
    private Account getRequiredActiveAccount(String accountId) {
        return findAccount(accountId)
                .orElseThrow(() -> new IllegalArgumentException("Account " + accountId + " does not exist or is dormant"));
    }

    /** Thread-safe transfer using double (convenience overload). */
    public void transfer(String fromAccountId, String toAccountId, double amount) {
        transfer(fromAccountId, toAccountId, BigDecimal.valueOf(amount));
    }

    /** Thread-safe transfer between two accounts with validation and deadlock-safe locking. */
    public void transfer(String fromAccountId, String toAccountId, BigDecimal amount) {
        validateAccountId(fromAccountId);
        validateAccountId(toAccountId);
        if (fromAccountId.equals(toAccountId)) {
            throw new IllegalArgumentException("Cannot transfer to the same account");
        }

        Objects.requireNonNull(amount, "amount must not be null");
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Transfer amount must be positive");
        }

        Account from = getRequiredActiveAccount(fromAccountId);
        Account to = getRequiredActiveAccount(toAccountId);

        // Always lock in a stable order to avoid deadlocks
        Account firstLock;
        Account secondLock;
        if (fromAccountId.compareTo(toAccountId) < 0) {
            firstLock = from;
            secondLock = to;
        } else {
            firstLock = to;
            secondLock = from;
        }

        synchronized (firstLock) {
            synchronized (secondLock) {
                if (from.balance.compareTo(amount) < 0) {
                    throw new IllegalArgumentException("Insufficient funds in account " + fromAccountId);
                }

                Transaction transaction = new Transaction(fromAccountId, toAccountId, amount);

                from.debit(amount);
                to.credit(amount);

                from.addTransaction(transaction);
                to.addTransaction(transaction);
            }
        }
    }

    /** Returns an immutable snapshot of the transaction history for a given account. */
    public List<Transaction> getTransactionHistory(String accountId) {
        Account account = getRequiredActiveAccount(accountId);
        return account.getTransactionsSnapshot();
    }

    private static void validateAccountId(String accountId) {
        if (accountId == null || accountId.isBlank()) {
            throw new IllegalArgumentException("accountId must not be null or blank");
        }
    }

    private static boolean isDormantAccountId(String accountId) {
        return accountId != null && accountId.startsWith(DORMANT_PREFIX);
    }

    public static void main(String[] args) {
        Bank bank = new Bank();
        bank.addAccount("A1", "John Doe", 1000.0);
        bank.addAccount("A2", "Jane Smith", 2000.0);

        bank.transfer("A1", "A2", 500.0);

        try {
            bank.transfer("A1", "A2", 600.0); // this will fail because of insufficient balance
        } catch (IllegalArgumentException ex) {
            System.err.println("Second transfer failed: " + ex.getMessage());
        }

        List<Transaction> transactions = bank.getTransactionHistory("A1");
        for (Transaction t : transactions) {
            System.out.println(t);
        }
    }

    /** Immutable, thread-safe view of an account's core state. */
    public static final class Account {
        private final String accountId;
        private final String accountHolder;
        private BigDecimal balance;
        private final List<Transaction> transactions = new ArrayList<>();

        private Account(String accountId, String holder, BigDecimal balance) {
            this.accountId = Objects.requireNonNull(accountId, "accountId must not be null");
            this.accountHolder = Objects.requireNonNull(holder, "accountHolder must not be null");
            this.balance = Objects.requireNonNull(balance, "balance must not be null");
        }

        public String getAccountId() {
            return accountId;
        }

        public String getAccountHolder() {
            return accountHolder;
        }

        public synchronized BigDecimal getBalance() {
            return balance;
        }

        private synchronized void credit(BigDecimal amount) {
            balance = balance.add(amount);
        }

        private synchronized void debit(BigDecimal amount) {
            balance = balance.subtract(amount);
        }

        private synchronized void addTransaction(Transaction transaction) {
            transactions.add(transaction);
        }

        /** Snapshot copy of transactions to preserve encapsulation and thread safety. */
        public synchronized List<Transaction> getTransactionsSnapshot() {
            return Collections.unmodifiableList(new ArrayList<>(transactions));
        }
    }

    /** Immutable transaction record. */
    public static final class Transaction {
        private final String fromAccountId;
        private final String toAccountId;
        private final BigDecimal amount;
        private final Instant timestamp;

        private Transaction(String from, String to, BigDecimal amount) {
            this.fromAccountId = Objects.requireNonNull(from, "fromAccountId must not be null");
            this.toAccountId = Objects.requireNonNull(to, "toAccountId must not be null");
            this.amount = Objects.requireNonNull(amount, "amount must not be null");
            this.timestamp = Instant.now();
        }

        public String getFromAccountId() {
            return fromAccountId;
        }

        public String getToAccountId() {
            return toAccountId;
        }

        public BigDecimal getAmount() {
            return amount;
        }

        public Instant getTimestamp() {
            return timestamp;
        }

        @Override
        public String toString() {
            return "Transaction from " + fromAccountId + " to " + toAccountId +
                    " of $" + amount + " at " + timestamp;
        }
    }

}


