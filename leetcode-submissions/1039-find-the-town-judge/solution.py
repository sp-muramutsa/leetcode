class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusted_people = [[] for _ in range(n + 1)]
        trusted_count = {i: 0 for i in range(n + 1)}

        for a, b in trust:
            trusted_people[a].append(b)
            trusted_count[b] += 1

        for person in range(1, n + 1):
            if not trusted_people[person] and trusted_count[person] == n - 1:
                return person

        return -1

