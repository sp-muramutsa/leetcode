class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            l = 0
            r = l + 1
            while l < r and r < len(nums):
                temp = nums[l]
                if nums[l] > nums[r]:
                    nums[l] = nums[r]
                    nums[r] = temp
                l += 1
                r += 1
