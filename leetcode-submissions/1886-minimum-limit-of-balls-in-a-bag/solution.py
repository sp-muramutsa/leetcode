class Solution:
    def can_split(self, nums, mid, max_ops) -> bool:

        num_ops = 0
        for num in nums:
            num_ops += (num - 1) // mid

        return num_ops <= max_ops

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        l, r = 1, max(nums)

        while l < r:
            mid = l + (r - l) // 2

            if self.can_split(nums, mid, maxOperations):
                r = mid
            else:
                l = mid + 1

        return l

