class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        solution = []

        def backtrack(i, curr_sum, nums_used, path):

            if nums_used == k:
                if curr_sum == n:
                    solution.append(path[:])
                return

            for j in range(i, 10):
                path.append(j)
                backtrack(j + 1, curr_sum + j, nums_used + 1, path)
                path.pop()

        backtrack(1, 0, 0, [])
        return solution

