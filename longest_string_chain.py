"""
Longest String Chain

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the
order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

"""
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=len)
        word_map = {}

        for word in sorted_words:
            word_map[word] = 1

        longest = 1
        for word in sorted_words:
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in word_map:
                    word_map[word] = max(word_map[prev] + 1, word_map[word])
                    longest = max(longest, word_map[word])
        return longest
