from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ """
        # Step 1: Counter hashmap: O(n)
        counter = Counter(nums)

        # Step 2: Build buckets based on frequency i.e. map of: frequency -> [list of values appearing that many times]
        n = len(nums)
        buckets = [[] for _ in range(n)]

        for value, frequency in counter.items():
            buckets[frequency - 1].append(value)

        # Step 3: Now we have buckets in a big bucket i.e. list of lists of the map. Iterate in it from back to front picking up the elements. Here the keys lies in the fact that we know the length of the original input list. And therefore the most frequent element can't have a frequency greater than that length. This effectively let's us have an O(n) runtime.
        result = []
        j = 0
        for i in range(n - 1, -1, -1):
            for number in buckets[i]:
                if j < k:
                    result.append(number)
                    j += 1
                else:
                    return result

        return result

