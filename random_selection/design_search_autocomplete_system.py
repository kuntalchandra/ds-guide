"""
Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a
special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences
that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences
have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences
is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed.
Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case
letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be
recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of
sentence already typed.


Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree.
Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we
only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following
input will be counted as a new search.

Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two
words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in
the historical data won't exceed 100.

Complexity:
AutocompleteSystem() takes O(k∗l) time. We need to iterate over l sentences each of average length k, to create the
trie for the given set of sentences.
input() takes O(p+q+mlogm) time. Here, p refers to the length of the sentence formed till now. q refers to the number
of nodes in the trie considering the sentence formed till now as the root node. Again, we need to sort the list of
length m indicating the options available for the hot sentences, which takes O(mlogm) time
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.hot = 0
        self.is_word = False


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):

        self.root = TrieNode()
        self.search_term = ""
        # Generate historical sentences
        for word, hot in zip(sentences, times):
            self.add(word, hot)

    def add(self, word: str, hot: int) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        # Later need to sort on hot, then ascii asc order
        node.hot -= hot

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add(self.search_term, 1)
            self.search_term = ""
        else:
            self.search_term += c
            return self.search()

    def search(self) -> List[str]:
        res = []
        node = self.root
        sentence = ""

        # Traverse till end of the search term
        for c in self.search_term:
            if c not in node.children:
                return res
            node = node.children[c]
            sentence += c

        # Once reached, dfs to find the possible matches
        self.dfs(node, sentence, res)
        if res:
            res.sort(key=lambda n: (n[0], n[1]))
            res = res[:3]
            res = [word for rank, word in res]
        return res

    def dfs(self, node: TrieNode, sentence: str, res: List[str]) -> None:
        # If node is end of the sentence, then add to res
        if node.is_word:
            res.append([node.hot, sentence])
        # Traverse till last child
        for c in node.children:
            self.dfs(node.children[c], sentence + c, res)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
