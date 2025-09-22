class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Using binary search
        # Perform binary search 
        # If not found return the index it should be in

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return l
