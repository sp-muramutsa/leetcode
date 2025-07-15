class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        solution = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, path, curr_sum):

            if curr_sum > target:
                return

            if curr_sum == target:
                solution.append(path[:])
                return

            for j in range(i, n):
                
                if j > i  and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                backtrack(j, path, curr_sum + candidates[j])
                path.pop()

        backtrack(0, [], 0)
        return solution

