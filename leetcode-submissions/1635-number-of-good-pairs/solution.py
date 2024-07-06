from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        Intuition: As we iterate through the list, we use a hashmap to count occurrences of each number.
                   For each number, the number of good pairs it forms is equal to the number of times it
                   has already appeared. We increment the good pairs count by this value and then update
                   the count of the current number in the hashmap.
        """

        hashmap = defaultdict(int)
        good_pairs = 0

        for number in nums:
            if number in hashmap:
                good_pairs += hashmap[number]
            hashmap[number] += 1

        return good_pairs

