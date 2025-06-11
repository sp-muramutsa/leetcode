class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
            
            elif nums[mid] <= nums[r]:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
        return -1
