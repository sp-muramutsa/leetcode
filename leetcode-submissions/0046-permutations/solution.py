class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Edge case if the length of curr is equal to the lenght of nums add curr to result and return
        # Create a for loop 
        # If the number is not eqaul to the current number and not in curr list
        # Add it to curr and reculsively call the function
        # After backtracking pop from curr and 
        # return 
        result = []
        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return 

            for i in range(len(nums)):
                if nums[i] in curr:
                    continue

                curr.append(nums[i])
                backtrack(curr)
                curr.pop()


            return 

        backtrack([])
        return result
