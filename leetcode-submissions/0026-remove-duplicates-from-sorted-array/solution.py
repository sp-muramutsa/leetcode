class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return

        l, r = 0, 1
        curr = nums[0]

        while r < n:
            if nums[r] == curr:
                r += 1
            else:
                nums[l + 1] = nums[r]
                curr = nums[l + 1]
                l += 1
                r += 1

        return l + 1

