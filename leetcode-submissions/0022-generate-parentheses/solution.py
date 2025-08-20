class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(path, starting_index):
            if starting_index / 2 == n:
                result.append("".join(path.copy()))
                return

            if path.count("(") < n:
                path.append("(")
                backtrack(path, starting_index+1)
                path.pop()

            if path.count(")") < path.count("("):
                path.append(")")
                backtrack(path, starting_index+1)
                path.pop()
        backtrack([], 0)
        return result
