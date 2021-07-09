"""
Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest
element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.


Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""
from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        """
        Time: O(n) for iteration. O(nLogn) for sort. For a sorted dataset, this time can't be acceptable.
        """
        if not matrix:
            return
        arr = []
        rows = len(matrix)
        for row in range(rows):
            arr.extend(matrix[row])
        arr.sort()
        return arr[k-1]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time Complexity: let X=min(K,N);X+Klog(X)
        The heap construction takes O(X) time. After that, performing K iterations and each iteration has two
        operations. Extract the minimum element from a heap containing X elements. Then add a new element to the heap.
        Both operations will take O(log(X)) time.
        Thus, the total time complexity comes down to be O(X+Klog(X)) where X is min(K,N).
        Space Complexity: O(X) which is occupied by the heap.
        """
        length = len(matrix)
        heap = []

        # prepare the min heap
        for row in range(min(k, length)):
            # add triplets of information for each cell and heapify the list
            heap.append((matrix[row][0], row, 0))
        heapify(heap)

        # until kthe element
        while k:
            # extract min
            element, r, c = heappop(heap)
            if c < (length - 1):
                heappush(heap, (matrix[r][c + 1], r, c + 1))

            # decrement k
            k -= 1
        return element
