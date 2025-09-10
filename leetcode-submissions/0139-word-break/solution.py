class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Iterative DP

        dictionary = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)

        for word in dictionary:
            if word[0] == s[0]:
                dp[0] = True

        if not dp[0]:
            return False

        for i in range(n):
            for word in dictionary:
                length = len(word)

                if i + length > n:
                    continue

                if dp[i] and s[i : i + length] == word:
                    dp[i + length] = True

        return dp[-1]

