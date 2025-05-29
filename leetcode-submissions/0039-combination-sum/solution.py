class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        def dfs(pointer, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if pointer >= len(candidates) or total > target:
                return 
            
            curr.append(candidates[pointer])
            dfs(pointer, total+candidates[pointer])
            curr.pop()
            dfs(pointer+1, total)
        dfs(0, 0)
        return res
