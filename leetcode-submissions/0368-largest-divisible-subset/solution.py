class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Create a dp for number of paths
        # Create a dp for paths
        # For loop the nums
        # Create the dps and set the first index to its number
        # Starting from index 1 
        # If it is divisible by the back numbers
        # If the path length of the index is greater than the carrier
        # Update the dp of paths and the dp length
        # Return the max path
        # In the loops have a current that checks the max length of the path
        # dp = [[1],[1,2],[1,2,4],[1,2,4,8]]
        # dp = [1,2,3,4]
        # [1,2,4,8]
        #      ^
        nums.sort()
        if len(nums) == 0:
            return []
        dp = [[i] for i in (nums)]
        dp[0] = [nums[0]]
        dp1 = [1] * len(nums)

        for i in range(1, len(nums)):
            print(i)
            carrier = 1
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if carrier <= dp1[j]:
                        dp[i] = dp[j] + [nums[i]]
                        carrier = dp1[j] + 1
                        dp1[i] = carrier
        print(dp)
        res = None
        ans = 0
        for i in dp:
            if len(i) > ans:
                res = i
                ans = len(i)
        return res
