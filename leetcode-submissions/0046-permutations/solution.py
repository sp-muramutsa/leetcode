class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Create a res variable
        res = []
        # Implement a dfs function
        def dfs(path):
            # Edge case if the length of the path is the same as the length of the nums add to result
            if len(path) == len(nums):
                res.append(path.copy())
            # Create a for loop for all nums
            for i in range(len(nums)):
                # If current number is in path skip it
                if nums[i] in path:
                    continue
                # After backtracking pop from the path
                path.append(nums[i])
                dfs(path)
                path.pop()

        dfs([])
        return res
