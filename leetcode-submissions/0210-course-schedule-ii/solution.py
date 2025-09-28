class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            in_degree[course] += 1
            adj[prereq].append(course)

        print(in_degree)
        print(adj)
        
        q = deque([course for course in range(numCourses) if in_degree[course] == 0])
        scheduling = []

        while q:

            curr = q.popleft()
            scheduling.append(curr)

            for dest in adj[curr]:
                in_degree[dest] -= 1

                if in_degree[dest] == 0:
                    q.append(dest)

        return scheduling if len(scheduling) == numCourses else []






