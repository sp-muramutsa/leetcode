class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Intuition: We move from left to right and when we see a non-zero value, we bring 
        it to the position of our left pointer
        """

        l, r, length = 0,  0, len(nums)

        while r < length:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
                
        
