"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order
of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to
lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less
than any other character
Approach:
Topological sorting
Wikipedia- A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that
for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of
the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed
before another; in this application, a topological ordering is just a valid sequence for the tasks. A topological
ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG).
Any DAG has at least one topological ordering, and algorithms are known for constructing a topological ordering of any
DAG in linear time.
Complexity AnalysisTime Complexity: O(C), where C is the total content of words.
Space Complexity: O(1)
"""
from typing import List
from unittest import TestCase


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_idx = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word = words[i]
            word_next = words[i + 1]

            # Identify the first difference between both the words
            min_len = min(len(word), len(word_next))
            for j in range(min_len):
                # Comparison doesn't match
                if word[j] != word_next[j]:
                    if ord_idx[word[j]] > ord_idx[word_next[j]]:
                        return False
                    break
            # No diff. But still check the compatibility for shorter words e.g. app and apple
            else:
                if len(word) > len(word_next):
                    return False
        return True


class TestVerifyAlieDictionary(TestCase):
    def setUp(self) -> None:
        self.words_1 = ["hello", "leetcode"]
        self.order_1 = "hlabcdefgijkmnopqrstuvwxyz"
        self.words_2 = ["word", "world", "row"]
        self.order_2 = "worldabcefghijkmnpqstuvxyz"
        self.words_3 = ["apap","app"]
        self.order_3 = "abcdefghijklmnopqrstuvwxyz"

    def test_verify_alien_dictionary(self) -> None:
        obj = Solution()
        self.assertTrue(obj.isAlienSorted(self.words_1, self.order_1))
        self.assertFalse(obj.isAlienSorted(self.words_2, self.order_2))
        self.assertTrue(obj.isAlienSorted(self.words_3, self.order_3))
