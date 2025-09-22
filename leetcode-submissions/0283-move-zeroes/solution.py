class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,3,0,0,0,12]

        # Create pointers left and right
        # Edge case; length of array less than 2 return array
        # Move until r is at the end
        # If right is a number and left is 0 swap the two and shift both by 1
        # If none of them is 0 move both by 1
        # If both are 0 shift just the right

        l, r = 0, 1

        while r < len(nums):
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
                continue
            elif (nums[r] != 0 and nums[l] != 0) or (nums[r] == 0 and nums[l] != 0):
                l += 1
                r += 1
                continue
                
            else:
                r += 1

        return nums

        
