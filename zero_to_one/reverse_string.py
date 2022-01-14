"""
Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


"""
Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and 
initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""


class Solution:
    def reverse_string(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join([elem for elem in s])

    def reverse_words_bruteforce(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = ""
        for word in words:
            reversed_words += self.reverse_string(word) + " "
        return reversed_words.strip(" ")

    def reverse_words(self, s: str) -> str:
        words = s.split(" ")
        return " ".join(word[::-1] for word in words)
