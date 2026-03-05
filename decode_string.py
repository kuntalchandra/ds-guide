"""
Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

Approach:
Stack is your explicit recursion for nested brackets.
On '[': push (current_string, current_count), reset both.
On ']': pop, multiply current_string by count, append to the popped string.
This handles arbitrary nesting depth naturally.

stack = []
current_str = ""
current_num = 0

for ch in s:
    if ch.isdigit():
        current_num = current_num * 10 + int(ch)    # multi-digit numbers
    elif ch == '[':
        stack.append((current_str, current_num))
        current_str, current_num = "", 0
    elif ch == ']':
        prev_str, repeat_count = stack.pop()
        current_str = prev_str + repeat_count * current_str
    else:
        current_str += ch

return current_str

Triggers:
- nested encoding/decoding
- "k[pattern]" style string expansion
- anything with matching brackets that carry a multiplier

Variants / Watch-outs:
- Multi-digit numbers: current_num = current_num * 10 + digit (not just int(ch))
- Reset current_num only after '[', not inside ']' handler
"""

from unittest import TestCase


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        text = ""
        for c in s:
            if c == "[":
                stack.append(text)
                stack.append(num)
                text = ""
                num = 0
            elif c == "]":
                num = stack.pop()
                prev_text = stack.pop()
                text = prev_text + text * num
                num = 0
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                text += c
        return text


class TestDecodeString(TestCase):
    def setUp(self) -> None:
        self.encoded_str = "3[a]2[bc]"

    def test_decode_string(self):
        obj = Solution()
        self.assertEqual(obj.decodeString(self.encoded_str),
                         "aaabcbc")
