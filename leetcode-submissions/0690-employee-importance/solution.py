"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:

        graph = defaultdict(list)
        importance_hashmap = {}
        for employee in employees:
            graph[employee.id] = employee.subordinates
            importance_hashmap[employee.id] = employee.importance

        def dfs(employee):
            nonlocal importance
            importance += importance_hashmap[employee]
            for neighbor in graph[employee]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        importance = 0
        for emp in employees:
            if emp.id == id:
                source = emp
                visited = {emp.id}
                dfs(emp.id)
                break

        return importance

