class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        candidates.sort()
        solution, path = set(), []

        def backtrack(i, path, curr_sum):

            if curr_sum == target:
                solution.add(tuple(path[:]))
                return

            if curr_sum > target:
                return

            for j in range(i + 1, n):
                
                if curr_sum + candidates[j] > target: 
                    break
                
                if j > i + 1 and candidates[j] == candidates[j - 1]:
                    continue


                path.append(candidates[j])
                curr_sum += candidates[j]
                backtrack(j, path, curr_sum)
                
                curr_sum -= candidates[j]
                path.pop()

        backtrack(-1, path, 0)
        res = [list(sol) for sol in solution]
        return res

