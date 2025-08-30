class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        def backtrack(i):

            if dp[i] != 0:
                return dp[i]

            # We go to the last digit: 1 valid decoding
            if i == n:
                return 1

            # 0 valid decodings 
            if s[i] == "0":
                return 0

            # Process this index
            dp[i] += backtrack(i + 1)

            # Process the next (double digits)
            if i < n - 1:
                nbr = int(s[i : i + 2])
                if 0 < nbr <= 26:
                    dp[i] += backtrack(i + 2)

            return dp[i]

        backtrack(0)
        return dp[0]

