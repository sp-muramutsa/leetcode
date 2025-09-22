class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Create a left and right pointer
        # [0,1,2,1,1,1,2,3,3,4]
        # Starting from the second value yoouo will shift the right pointer until the value one step back from left is less than
        # Swap the numbers
        # Shif both left and right by 1
        if len(nums) == 0:
            return 0


        l, r = 1, 1
        res = 0

        while r < len(nums):
            if nums[l] <= nums[l-1]:
                while r < len(nums) and nums[r] <= nums[l-1]:
                    r += 1
                
                if r < len(nums):
                    nums[l], nums[r] = nums[r], nums[l]
            if r < len(nums):
                l += 1
                r += 1

        return l

        
