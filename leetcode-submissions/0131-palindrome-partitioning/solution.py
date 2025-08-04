class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # If the starting index has reached add the path and then end return
        # Create a loop for the index
        # If the prefix is not a palindrome continue
        # If it is add to the path and operate dfs function
        result = []
        n = len(s)
        def is_palindrome(l):
            return l == l[::-1]
        def dfs(starting_index, path):
            if starting_index == n:
                result.append(path.copy())
                return

            for i in range(starting_index+1, n+1):
                prefix = s[starting_index:i]
                if is_palindrome(prefix):
                    path.append(prefix)
                    dfs(i, path)
                    path.pop()
                
        dfs(0, [])
        return result
