class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        # Bisect left
        # First occurence. Left: nums[mid] < target

        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if 0 <= l < n and nums[l] == target:
            left, right = l, n
            first = l  # First False
        else:
            return [-1, -1]

        # Last occurence. Left: nums[mid] == target
        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                left = middle + 1
            else:
                right = middle

        last = left - 1  # Last True
        if 0 <= last < n and nums[left - 1] == target:
            return [first, last]
        else:
            return [-1, -1]

