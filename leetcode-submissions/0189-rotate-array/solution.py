class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # Reverse the list
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Reverse the first k elements
        l, r = 0, k - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            r -= 1
            l += 1

        # Rverse he rest of the elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            r -= 1
            l += 1
