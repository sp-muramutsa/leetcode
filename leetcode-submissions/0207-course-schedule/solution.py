class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        in_degree = [0] * numCourses
        adj = defaultdict(list)

        for dest, src in prerequisites:
            in_degree[dest] += 1
            adj[src].append(dest)
        
        q = deque([course for course in range(numCourses) if in_degree[course] == 0])
        scheduled = 0

        while q:

            curr = q.popleft()
            scheduled += 1

            for course in adj[curr]:
                in_degree[course] -= 1

                if in_degree[course] == 0:
                    q.append(course)
        
        return scheduled == numCourses



