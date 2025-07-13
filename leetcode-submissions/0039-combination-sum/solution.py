class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        solution, path = [], []
        
        def backtrack(i, path):

            if sum(path) == target:
                sol = Counter(path)
                if sol not in solution:
                    solution.append(sol)
                return    
            
            if sum(path) > target:
                return 

            for num in candidates:     
                path.append(num)
                backtrack(i + 1, path)
                path.pop()
        
        
        backtrack(0, [])
        res = []
        for sol in solution:
            combination = []
            for key, value in sol.items():
                for _ in range(value):
                    combination.append(key)
            res.append(combination)
            
        return res
        
        return []
