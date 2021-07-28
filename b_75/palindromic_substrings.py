"""
Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of
same characters.
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"

Time/ Space: O(n^2) / O(1)
Why?
Time Complexity: O(N^2) for input string of length NN. The total time taken in this approach is dictated by
two variables:
    The number of possible palindromic centers we process.
    How much time we spend processing each center.
The number of possible palindromic centers is 2N-1: there are N single character centers and N-1 consecutive
character pairs as centers.

Each center can potentially expand to the length of the string, so time spent on each center is linear on average.
Thus total time spent is N * (2N-1) ~= N^2
Space Complexity: O(1). We don't need to allocate any extra space since we are repeatedly iterating on the input
string itself.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        for center in range(2 * length - 1):
            left = center // 2
            right = (center + 1) // 2

            while left >= 0 and right < length and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
