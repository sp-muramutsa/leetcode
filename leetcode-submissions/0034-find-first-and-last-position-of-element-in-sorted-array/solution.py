class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.BinSearch(nums, True, target)
        right = self.BinSearch(nums, False, target)
        return [left, right]
    def BinSearch(self, nums, left_bias, target):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                if left_bias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i
