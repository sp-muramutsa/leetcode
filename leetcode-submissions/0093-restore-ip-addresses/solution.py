class Solution:
    def is_valid(self, s: str) -> bool:

        if not s:
            return False

        if int(s) > 255:
            return False

        if s[0] == "0" and len(s) > 1:
            return False

        return True

    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        if n > 12:
            return []

        solution = []

        def backtrack(i, dots, path):

            if dots == 4 and i == n:
                solution.append(".".join(path))
                return

            for j in range(i, min(i + 3, n)):
                if self.is_valid(s[i : j + 1]):
                    path.append(s[i : j + 1])
                    backtrack(j + 1, dots + 1, path)
                    path.pop()

        backtrack(0, 0, [])
        return solution

