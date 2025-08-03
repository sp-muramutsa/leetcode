class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[p].append(c)

        visited = [False] * numCourses
        in_degree = [0] * numCourses

        # Set in degrees
        for c, p in prerequisites:
            in_degree[c] += 1

        # Khan's Algorithm for Topological sort
        q = deque()
        schedule = []

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:

            # Process front node
            prereq = q.popleft()
            schedule.append(prereq)
            visited[prereq] = True

            # Reduce in degree of dependent courses
            for dependent in adj[prereq]:
                in_degree[dependent] -= 1

                if in_degree[dependent] == 0 and not visited[dependent]:
                    q.append(dependent)

        # All courses should be scheduled
        return not any(course == False for course in visited)

