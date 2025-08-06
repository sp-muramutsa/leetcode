class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Create a list for visited
        # Create a result list
        # Define the dfs function
        # If the length of the path is length of the nums add the path to result
        # Create a for loop for possible decisions
        # If the current number is not visited
        # Turn it to visited
        # Dfs 
        # After backtracking pop from the path
        # Turn visited index back to False
        visited_decisions = [False] * len(nums)
        result = []
        length = len(nums)
        def dfs(path):
            if len(path) == length:
                result.append(path.copy())
                return

            for i, n in enumerate(nums):
                if visited_decisions[i] == False:
                    visited_decisions[i] = True
                    path.append(n)
                    dfs(path)
                    visited_decisions[i] = False
                    path.pop()
        dfs([])
        return result
