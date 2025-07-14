class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        solution, path = [], []

        def backtrack(open_count, close_count):
            
            if open_count == n and close_count == n:
                solution.append("".join(path))
                return
            
            if close_count > open_count:
                return
            
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()
            
            if close_count < n:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()
        
        backtrack(0, 0)
        return solution

