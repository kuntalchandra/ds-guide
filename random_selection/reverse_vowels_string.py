"""
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        # set literal vowels = {"a", "e", "i", "o", "u"}
        vowels = set(["a", "e", "i", "o", "u"])

        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
