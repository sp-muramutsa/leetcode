class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # [1, 3, 4, 2, 2]
        # [1, 2, 3, 4, 5]
        # [1, 3, 4, 5, 6]
        # [T, F, F, F, F]
        # return first False

        def less_or_equal_count(number: int) -> bool:
            count = 0
            for x in nums:
                if x <= number:
                    count += 1
            return count <= number

        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if less_or_equal_count(mid):
                l = mid + 1
            else:
                r = mid

        return l

