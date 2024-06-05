from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Intuition:
        1. Use a Counter to count occurrences of each number.
        2. Identify numbers that have duplicates by checking counts greater than one.
        3. Create a hashmap to store the indices of these duplicate numbers.
        4. Check the differences between the indices of each duplicate number to see if any are within k distance.
        """

        counter = Counter(nums)
        n = len(nums)
        duplicates = set()

        # Find elements that appear more than once
        for key, value in counter.items():
            if value > 1:
                duplicates.add(key)

        # Store indices of duplicate elements in a hashmap
        hashmap = {}
        for i in range(n):
            if nums[i] in duplicates:
                if nums[i] not in hashmap:
                    hashmap[nums[i]] = [i]
                else:
                    hashmap[nums[i]].append(i)

        # Check if any two indices of the same element are within distance k
        for indexes in hashmap.values():
            m = len(indexes)
            l, r = 0, 1
            while r < m:
                if indexes[r] - indexes[l] <= k:
                    return True
                l += 1
                r += 1

        return False

