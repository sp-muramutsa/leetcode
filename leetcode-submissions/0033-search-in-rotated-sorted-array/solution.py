class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            # [4,5,6,7,0,1,2]
            # Left: sorted part
            if nums[mid] >= nums[0]:
                # If target is left, search here
                if nums[0] <= target < nums[mid]:
                    r = mid 
                else:
                    l = mid + 1
            
            # Right: rotated part
            else:
                # If target is right, search here
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid 
        
        
        return l if nums[l] == target else -1
