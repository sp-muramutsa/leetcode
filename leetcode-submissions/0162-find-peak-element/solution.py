class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums = [float("-inf")] + nums + [float("-inf")]
        n = len(nums)
        l, r = 1, n

        while l < r:
            mid = l + (r - l) // 2
           
            if nums[mid] <= nums[mid - 1]:
                r = mid
            
            elif nums[mid] <= nums[mid + 1]:
                l = mid + 1
            
            else:
                return mid - 1
