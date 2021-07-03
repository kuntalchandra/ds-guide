"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by
an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of
fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while
moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
Example 4:

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can pick from trees [1,2,1,1,2].
Time complexity: O(n)

Note: Check the implementation of longest substring with k distinct char
"""
from collections import defaultdict
from unittest import TestCase


class Solution(object):
    def totalFruit(self, tree):
        tracker = defaultdict(int)
        start = result = 0

        for end in range(len(tree)):
            tracker[tree[end]] += 1
            while len(tracker) > 2:
                tracker[tree[start]] -= 1
                if tracker[tree[start]] == 0:
                    del tracker[tree[start]]
                start += 1
            result = max(result, end - start + 1)
        return result


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.tree_1 = [1, 2, 1]
        self.tree_2 = [0, 1, 2, 2]
        self.tree_3 = [1, 2, 3, 2, 2]
        self.tree_4 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

    def test_total_fruit(self) -> None:
        obj = Solution()
        self.assertEqual(3, obj.totalFruit(self.tree_1))
        self.assertEqual(3, obj.totalFruit(self.tree_2))
        self.assertEqual(4, obj.totalFruit(self.tree_3))
        self.assertEqual(5, obj.totalFruit(self.tree_4))