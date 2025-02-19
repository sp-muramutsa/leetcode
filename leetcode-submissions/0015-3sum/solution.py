class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^2)
        Space: O(n) - for the result set and input space if sorting in-place is not considered extra space.
        Intuition:
        1. Sort the array to use a two-pointer technique efficiently.
        2. Iterate through the array, and for each element, use two pointers to find the remaining two elements that sum up to zero.
        3. Skip duplicates to ensure all triplets are unique.
        """

        nums.sort()  # Sort the input list to apply two-pointer technique
        i, n = 0, len(nums)
        result = set()  # Use a set to avoid duplicate triplets

        while i < n:
            l, r = i + 1, n - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

            i += 1

        return list(result)

