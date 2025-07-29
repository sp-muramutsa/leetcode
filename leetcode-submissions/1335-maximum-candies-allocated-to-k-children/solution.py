class Solution:
    def is_correct_partition(self, candies, rate, k):

        maxes = 0
        for c in candies:
            maxes += c // rate

        return maxes >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:

        l, r = 1, max(candies) + 1

        while l < r:
            rate = l + (r - l) // 2
            if self.is_correct_partition(candies, rate, k):
                l = rate + 1
            else:
                r = rate

        return l - 1

