"""
Strobogrammatic Number

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true

"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        left, right = 0, len(num) - 1

        while left <= right:
            if (num[left], num[right]) not in maps:
                return False
            left += 1
            right -= 1
        return True
