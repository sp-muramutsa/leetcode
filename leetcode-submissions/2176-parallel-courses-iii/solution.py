class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        in_degree = [0 for _ in range(n + 1)]

        for prev_course, next_course in relations:
            adj[prev_course].append(next_course)
            in_degree[next_course] += 1

        q = deque([course for course in range(1, n + 1) if in_degree[course] == 0])
        max_time = [time[course] for course in range(n)]

        while q:

            schedule = deque()
            k = len(q)

            for _ in range(k):
                prereq = q.popleft()

                in_degree[prereq] = -1

                for course in adj[prereq]:
                    in_degree[course] -= 1
                    max_time[course - 1] = max(max_time[prereq - 1] + time[course - 1], max_time[course - 1])

                    if in_degree[course] == 0:
                        schedule.append(course)

            q = schedule

        return max(max_time)

