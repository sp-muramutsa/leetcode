class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        solution, path = [], []
        
        def backtrack(i):

            if i == n + 1: 
                if len(path) == k:
                    solution.append(path.copy())
                return
            
            backtrack(i + 1)

            path.append(i)
            backtrack(i + 1)
            path.pop()
        
        backtrack(1)
        return solution

        
       

