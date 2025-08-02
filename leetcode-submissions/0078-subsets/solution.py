class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # If the counter reaches the kength of the list add result to result list
        # Add the number to the lsit and keep running the function
        # After the function backtracks skip the current number and go to the next
        # Return the result
        def backtrack(num, res, nums, curr):
            if num == len(nums):
                res.append(curr.copy())
                return 

            curr.append(nums[num])
            backtrack(num+1, res, nums, curr)
            curr.pop()
            backtrack(num+1, res, nums, curr)

        result = []
        backtrack(0, result, nums, [])
        return result
