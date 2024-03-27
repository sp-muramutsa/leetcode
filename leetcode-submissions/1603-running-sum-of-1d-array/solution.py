class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        """
        Time: O(n)
        Space: O(1)
        """

        length = len(nums)
        for i in range(1, length):
            nums[i] = nums[i-1] + nums[i]
        
        return nums
        
