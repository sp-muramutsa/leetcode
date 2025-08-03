class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Khan's algorithm for Topological Sort in Directed Acyclic Graphs (and cycle detection in cyclic ones)
        """

        # Adjacency list: course -> prerequisite

        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[p].append(c)

        schedule = deque()
        visited = {course: False for course in range(numCourses)}

        # Calculate in degrees i.e. number of prereqs per course
        in_degree = {course: 0 for course in range(numCourses)}
        for c, p in prerequisites:
            in_degree[c] += 1

        # Enqueue courses with no prereqs
        q = deque()
        for destination in in_degree:
            if in_degree[destination] == 0:
                q.append(destination)

        # Khan's algorithm for Topological Ordering
        while q:

            curr = q.popleft()
            visited[curr] = True
            schedule.append(curr)

            for course in adj[curr]:
                in_degree[course] -= 1

                if in_degree[course] == 0 and not visited[course]:
                    q.append(course)

        if any(not visited[course] for course in visited):
            return []

        return list(schedule)

