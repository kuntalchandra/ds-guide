"""
Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property
where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]

"""

from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller1(self, nums: List[int]) -> List[int]:
        """
        Due to list insertion O(n), this solution is O(n^2), but still better than the naive
        one to traverse using 2 loops
        """
        temp, res = [], []
        for num in nums[::-1]:  # O(n)
            idx = bisect_left(temp, num)    # O(logn) to find the index where this element should belong to
            res.insert(0, idx)  # n elements count == idx
            temp.insert(idx, num)   # keep the temp ready for the next lookup
        return res

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        O(Nlog(N)) and O(N)
        """
        length = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]  # record value => index
        res = [0] * length

        def merge_sort(arr: List[int], left: int, right: int):
            # in-place asc order sort
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left: int, right: int, mid: int):
            # merge from left -> mid and mid -> right
            i = left  # current idx of the left array
            j = mid  # current idx of the right array
            temp = []  # temporary placeholder to store the sorted array
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid are numbers shift to the left of arr[i]
                    res[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # if still left array has elements
            while i < mid:
                res[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, length)
        return res