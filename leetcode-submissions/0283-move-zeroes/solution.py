class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Intuition: Move non-zeros then move zeros after
        """

        n = len(nums)

        i = 0
        for number in nums:
            if number != 0:
                nums[i] = number
                i += 1
        
        j = n - i
        for k in range(1, j+1):
            nums[-k] = 0

        
        
        





