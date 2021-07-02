"""
Employee Importance
You have a data structure of employee information, which includes the employee's unique id, their importance value, and
their direct subordinates' id.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this employee and all
their subordinates.

Time complexity: O(n), space complexity: O(n), where n is the number of employees.
"""
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        imp_map = {}
        s_ord_map = {}
        for employee in employees:
            imp_map[employee.id] = employee.importance
            s_ord_map[employee.id] = employee.subordinates
        return self.helper(id, imp_map, s_ord_map)

    def helper(self, id: int, imp_map: Dict[int, int], s_ord_map: Dict[int, List[int]]) -> int:
        res = imp_map[id]
        for s_ord in s_ord_map[id]:
            res += self.helper(s_ord, imp_map, s_ord_map)
        return res
