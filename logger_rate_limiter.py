"""
Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only
be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from
being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given
timestamp, otherwise returns false.

Example 1:

Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]
"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.log_map:
            if timestamp < self.log_map[message] + 10:
                return False
        self.log_map[message] = timestamp
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
