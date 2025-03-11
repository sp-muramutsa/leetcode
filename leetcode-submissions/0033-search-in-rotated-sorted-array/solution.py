class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.getPivotIndex(nums)
        n = len(nums)

        # Binary search on the left of the pivot
        target_index = self.binary_search(0, min_index, nums, target)

        # If not found on the left, search on the right or return -1
        if target_index != -1:
            return target_index
        else:
            return self.binary_search(min_index, n - 1, nums, target)

    def binary_search(self, l, r, nums, target):
        while l <= r:
            mid = l + (r - l) // 2
            print("Mid", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    def getPivotIndex(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return l

