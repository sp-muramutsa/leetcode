class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # Bisect left
        # All single elements are at even indices
        # [2, 2, 3, 3, 7, 7, 10, 11, 11, 12, 12]
        # Is nums[i] == nums[i + 1]
        # [T, _, T, _, T, _, F, _, F, _, F] -> Return the first False. 
        # Only selecting even indices: retuce mid by 1 if it's even and add 2 to left
        # Left: nums[i - 1] < nums[i] == nums[i + 1]

        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2
            if mid % 2 == 1:
                mid -= 1

            # Left
            if nums[mid] == nums[mid + 1]:
                l = mid + 2

            # Right
            else:
                r = mid

        return nums[l]

