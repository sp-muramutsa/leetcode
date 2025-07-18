class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        solution = []
        n = len(s)

        def backtrack(i, path):

            if i == n:
                solution.append(path[:])
                return

            for j in range(i + 1, n + 1):
                if self.is_palindrome(s[i:j]):
                    path.append(s[i:j])
                    backtrack(j, path)
                    path.pop()
           

        backtrack(0, [])
        return solution

