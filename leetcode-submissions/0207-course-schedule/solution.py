from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Hashmap for in-degree
        in_degree = {i: 0 for i in range(numCourses)}
        dependants = [[] for _ in range(numCourses)]

        # Set the in-degree values and also dependants
        for child, parent in prerequisites:
            in_degree[child] += 1
            dependants[parent].append(child)

        # Khan's Algorithm
        queue = deque()
        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)
        
        res = []

        while queue:
            n = queue.popleft()
            res.append(n)
            for neighbor in dependants[n]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return len(res) == numCourses

