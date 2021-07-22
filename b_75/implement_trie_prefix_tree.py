"""
Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False  # True for the end of the trie word


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Time complexity : O(m), where m is the key length. In each iteration of the algorithm, either examine or create
        a node in the trie till reach the end of the key. This takes only m operations.
        Space complexity : O(m). In the worst case newly inserted key doesn't share a prefix with the the keys already
        inserted in the trie. We have to add m new nodes, which takes us O(m) space.
        """
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        Time complexity : O(m) In each step of the algorithm we search for the next key character. In the worst case
        the algorithm performs m operations. Space complexity : O(1)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children.get(char)
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children.get(char)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
