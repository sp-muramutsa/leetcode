class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        adj = [[] for _ in range(n + 1)]
        in_degree = [0 for _ in range(n + 1)]

        for prev_course, next_course in relations:
            adj[prev_course].append(next_course)
            in_degree[next_course] += 1

        q = deque([course for course in range(1, n + 1) if in_degree[course] == 0])

        semesters = 0
        scheduled_count = 0

        while q:
            semesters += 1
            schedule = deque()
            k = len(q)
            for _ in range(k):
                prereq = q.popleft()
                in_degree[prereq] = -1
                scheduled_count += 1

                for course in adj[prereq]:
                    in_degree[course] -= 1

                    if in_degree[course] == 0:
                        schedule.append(course)

            q = schedule

        return semesters if scheduled_count == n else -1

