class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Time: O(nlogn)
        Space: O(1)
                Intuition: Sort the array and use two pointers. For each pair (nums[l], nums[r])
                where nums[l] + nums[r] <= target, count the number of valid subsequences
                using the formula 2^(r - l).
        """

        nums.sort()
        l, r = 0, len(nums) - 1
        result = 0
        mod = (10**9) + 7

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                result += pow(2, r - l)  # This is where the sugar is !!!!!! Power 2 bc each element in this range can either be included or not.
                l += 1

        return result % mod

