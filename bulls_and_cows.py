"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you
provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong
position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both
secret and guess may contain duplicate digits.


Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to
allow one 1 to be a bull.

Example 3:
Input: secret = "1", guess = "0"
Output: "0A0B"

Example 4:
Input: secret = "1", guess = "1"
Output: "1A0B"
"""
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_map = defaultdict(int)
        guess_map = defaultdict(int)
        bull, cow = 0, 0

        for sec, gs in zip(secret, guess):
            if sec == gs:
                bull += 1
            else:
                secret_map[sec] += 1
                guess_map[gs] += 1

        for k in guess_map:
            cow += min(secret_map[k], guess_map[k])
        return str(bull) + "A" + str(cow) + "B"
