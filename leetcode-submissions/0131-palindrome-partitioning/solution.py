class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(idx, path):
            if idx == len(s):
                res.append(path.copy())
                return

            for i in range(idx, len(s)):
                prefix = s[idx:i+1]
                if prefix[:] == prefix[::-1]:
                    path.append(prefix)
                    dfs(i+1, path)
                    path.pop()

        dfs(0, [])
        return res

