class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
                Time: O(nlogn)
                Space: O(n)
                Intuition: To minimize the difference between the highest and lowest scores of any
        \U0001d458
        k students, first sort the array of scores. Then, use a sliding window of size
        \U0001d458
        k to traverse the sorted array, calculating the difference between the highest and lowest scores within each window. Track the smallest difference encountered. This approach ensures that exactly
        \U0001d458
        k scores are considered and identifies the group with the smallest possible range between the highest and lowest scores.
        """

        length = len(nums)
        nums.sort(reverse=True)
        l, r = 0, k - 1
        minimized = abs(nums[r] - nums[l])

        while r < length:
            difference = abs(nums[r] - nums[l])
            minimized = min(minimized, difference)
            l += 1
            r += 1

        return minimized

