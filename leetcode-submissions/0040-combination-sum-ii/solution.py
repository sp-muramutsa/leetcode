class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        candidates.sort()
        solution = []

        def backtrack(i, path, curr_sum):
            if curr_sum == target:
                solution.append(path[:])
                return
            
            if curr_sum > target:
                return

            for j in range(i, n):
                
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                 
                path.append(candidates[j])
                backtrack(j + 1, path, curr_sum + candidates[j])
                path.pop()  

        backtrack(0, [], 0) 
        return solution

