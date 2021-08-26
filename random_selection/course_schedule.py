"""
Course Schedule

There are a total of num_courses courses you have to take, labeled from 0 to num_courses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: num_courses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: num_courses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it
is impossible.



Time Complexity: O(∣E∣+∣V|^2) where |E| is the number of dependencies, ∣V∣ is the number of courses and d is the
maximum length of acyclic paths in the graph
Space Complexity: O(∣E∣+∣V∣)

Optimisation: Instead of backtracking, if we have used Postorder DFS backtracking or topological sorting approach then
time complexity gets reduced to O(∣E∣+∣V∣)
"""
from collections import defaultdict
from typing import Dict, List


class Solution:
    def __init__(self):
        self.not_checked = 0
        self.checking = 1
        self.checked = 2

    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        required_courses = defaultdict(list)

        for course, required in prerequisites:
            required_courses[course].append(required)

        states = [self.not_checked for _ in range(num_courses)]

        for course in range(num_courses):
            if self.has_deadlock(course, states, required_courses):
                return False
        return True

    def has_deadlock(self, course: int, states: List[int], required_courses: Dict[int, List]):
        if states[course] == self.checking:
            return True
        if states[course] == self.checked:
            return False
        states[course] = self.checking
        for required_course in required_courses[course]:
            if self.has_deadlock(required_course, states, required_courses):
                return True
        states[course] = self.checked
        return False


"""
Course Schedule II

There are a total of num_courses courses you have to take, labeled from 0 to num_courses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take 
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of 
them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: num_courses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the 
correct course order is [0,1].
Example 2:

Input: num_courses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: num_courses = 1, prerequisites = []
Output: [0]

"""


class Solution1:
    def __init__(self):
        self.not_checked = 0
        self.checking = 1
        self.checked = 2
        self.orders = []

    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        required_courses = defaultdict(list)

        for course, required in prerequisites:
            required_courses[course].append(required)

        states = [self.not_checked for _ in range(num_courses)]

        for course in range(num_courses):
            if self.deadlock(course, states, required_courses):
                return []
        return self.orders

    def deadlock(self, course: int, states: List[int], required_courses: List[List[int]]) -> bool:
        if states[course] == self.checked:
            return False
        if states[course] == self.checking:
            return True
        states[course] = self.checking
        for required_course in required_courses[course]:
            if self.deadlock(required_course, states, required_courses):
                return True
        states[course] = self.checked
        self.orders.append(course)
        return False
