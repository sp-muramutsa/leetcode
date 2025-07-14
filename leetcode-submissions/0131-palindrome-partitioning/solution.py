class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        
        solution, path = [], []
        n = len(s)

        def backtrack(i):
            if i == n:
                if "".join(path) == s:
                    ans = path[1:]
                    if ans:
                        solution.append(ans)
                return

            for j in range(i + 1, n + 1):
                if self.is_palindrome(s[i:j]):
                    path.append(s[i:j])
                    backtrack(j)
                    path.pop()

        backtrack(-1)
        return solution

