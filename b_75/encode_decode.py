"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized
enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode
algorithm.
"""
from unittest import TestCase


class Solution:
    def encode(self, s: str) -> str:
        if not s:
            return ""
        encoded = ""
        for char in s:
            encoded += char.replace("/", "#/#") + "//"
        return encoded

    def decode(self, s: str) -> str:
        if not s:
            return ""
        decoded = ""
        s = s.split("//")
        for char in s:
            decoded += char.replace("#/#", "/")
        return decoded


class TestEncodeDecode(TestCase):
    def setUp(self) -> None:
        self.str_1 = "abcd"
        self.str_2 = "ab/cd"
        self.str_3 = ""
        self.str_4 = "ab cd ef"
        self.str_5 = "ab . / cd /"

    def test_encode_decode(self) -> None:
        obj = Solution()
        self.assertEqual(self.str_1, obj.decode(obj.encode(self.str_1)))
        self.assertEqual(self.str_2, obj.decode(obj.encode(self.str_2)))
        self.assertEqual(self.str_3, obj.decode(obj.encode(self.str_3)))
        self.assertEqual(self.str_4, obj.decode(obj.encode(self.str_4)))
        self.assertEqual(self.str_5, obj.decode(obj.encode(self.str_5)))
