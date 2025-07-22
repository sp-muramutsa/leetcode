class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find the first occurence
        # Is number less than target?
        # [T, T, T, T, [F], F, F, F] -> First F

        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if 0 <= l < n and nums[l] == target:
            start = l
        else:
            return [-1, -1]

        lo, hi = l, n

        # Last first occurence
        # Is number equal target?
        # [T, T, T, T, [F], F, F, F] -> First F
        while lo < hi:
            middle = lo + (hi - lo) // 2

            if nums[middle] == target:
                lo = middle + 1
            else:
                hi = middle

        if 0 <= lo <= n and nums[lo - 1] == target:
            print(start)
            return [start, lo - 1]

        return [-1, -1]

