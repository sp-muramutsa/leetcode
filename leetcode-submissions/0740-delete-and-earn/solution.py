class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        last = max(nums)
        n = len(nums)
        counter = collections.Counter(nums)

        for element, count in counter.items():
            counter[element] = element * counter[element]

        dp = [0] * (last + 1)

        dp[0] = counter.get(0, 0)
        dp[1] = max(dp[0], counter.get(1, 0))

        for i in range(2, last + 1):
            dp[i] = max(dp[i - 1], counter.get(i, 0) + dp[i - 2])

        return dp[-1]

