class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We have two options either we add ( or we add )
        # If the end of the path is reached we add the path to the result
        # If the opening is less than the required opening
        # Add the ( to path and dfs
        # Backtrack and pop
        # If the closing is less than the expeced closing 
        # dfs backtracka and pop
        result = []
        def dfs(starting_index, closing, opening, path):
            if starting_index == 2 * n:
                result.append("".join(path.copy()))
                return

            if opening < n:
                path.append('(')
                dfs(starting_index+1, closing, opening+1, path)
                path.pop()

            if closing < opening:
                path.append(')')
                dfs(starting_index+1, closing+1, opening, path)
                path.pop()

        dfs(0, 0, 0, [])
        return result
