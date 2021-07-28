"""
Course Schedule I

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So it is possible.
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take
course 0 you should also have finished course 1. So it is impossible.
Approach: DFS Cyce detection. Refer to Topological sorting.
"""
from collections import defaultdict
from typing import Dict, List


class Solution:
    def __init__(self):
        self.not_checked = 0
        self.checking = 1
        self.checked = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirement = defaultdict(list)

        # get the list of requirement for each courses
        for course, required in prerequisites:
            requirement[course].append(required)

        # initialise the state of the courses
        states = [self.not_checked for _ in range(numCourses)]

        # find possibility
        for course in range(numCourses):
            if self.has_deadlock(course, requirement, states):
                return False
        return True

    def has_deadlock(self, course: int, requirement: Dict[int, List[int]], states: List[int]) -> bool:
        # deadlock cycle
        if states[course] == self.checking:
            return True
        # finished checking
        elif states[course] == self.checked:
            return False

        # update state
        states[course] = self.checking
        for required_course in requirement[course]:
            # if course has already checked
            if self.has_deadlock(required_course, requirement, states):
                return True

        # finished checking
        states[course] = self.checked
        return False


"""
Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.
Example 1:
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
is represented.
You may assume that there are no duplicate edges in the input prerequisites.
Approach:
Official LC explanation is worth to read. In a gist, it's an extension of Course Schedule 1 problem and the approach
would be topological sort again.
DFS Time Complexity should be O(2E +V), because DFS traversal is E+V and building graph is E. And Space complexity
should be O(E + 3V), where building graph is E + V, DFS function calls are V and the final V comes from visited.
"""
from collections import defaultdict


class Solution:
    def __init__(self):
        self.not_checked = 0
        self.checking = 1
        self.checked = 2
        self.res_order = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requirements = defaultdict(list)
        states = [self.not_checked for _ in range(numCourses)]
        for course, required in prerequisites:
            requirements[course].append(required)

        for course in range(numCourses):
            if not self.deadlock(course, requirements, states):
                return []
        return self.res_order

    def deadlock(self, course: int, requirements: Dict[int, List[int]], states: List[int]) -> bool:
        if states[course] == self.checking:
            return True
        if states[course] == self.checked:
            return False

        states[course] = self.checked
        for required in requirements[course]:
            if not self.deadlock(required, requirements, states):
                return False

        states[course] = self.checking
        self.res_order.append(course)
        return True
