"""
Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the
combinations may be returned in any order.



Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are
no valid combination.

Example 4:
Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.

Time: O(9!⋅K/(9−K)!)
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.backtrack(n, [], 0, k, [])

    def backtrack(self, remain: int, combination: List[List[int]], next_start: int, k: int, res: List[List[int]]):
        # it's a match
        if len(combination) == k and remain == 0:
            res.append(list(combination))
            return
        # exceeded the scope
        elif len(combination) == k or remain < 0:
            return

        # iterate through the reduced list of combinations
        for i in range(next_start, 9):
            combination.append(i + 1)
            self.backtrack(remain - i - 1, combination, i + 1, k, res)
            # backtrack the current combination
            combination.pop()
        return res


"""
Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the 
given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]
"""


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.backtrack(target, [], 0, [], candidates)

    def backtrack(self, remain: int, combination: List[List[int]], next_start: int, res: List[List[int]],
                  candidates: List[int]):
        if remain == 0:
            res.append(list(combination))
            return
        elif remain < 0:
            return

        for i in range(next_start, len(candidates)):
            combination.append(candidates[i])
            self.backtrack(remain - candidates[i], combination, i, res, candidates)
            combination.pop()
        return res
