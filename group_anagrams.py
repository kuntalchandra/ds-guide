"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer
loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
Space Complexity: O(NK), the total information content stored in ans.
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        res = defaultdict(list)
        for word in strs:
            word_tuple = tuple(sorted(word))
            res[word_tuple].append(word)
        return [words for key, words in res.items()]
        # return res.values()
