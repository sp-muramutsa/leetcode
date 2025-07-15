class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        solution = []

        def backtrack(i, nums_used, path):
            if nums_used == k:
                solution.append(path[:])
                return

            for j in range(i, n + 1):
                path.append(j)
                backtrack(j + 1, nums_used + 1, path)
                path.pop()

        backtrack(1, 0, [])
        return solution

