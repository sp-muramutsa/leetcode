class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashmap = collections.defaultdict(int)
        hashmap[0] = 1

        cum_sum = 0
        count = 0
        n = len(nums)

        for i in range(n):
            cum_sum += nums[i]

            complement = cum_sum - k
            if complement in hashmap:
                count += hashmap[complement]

            hashmap[cum_sum] += 1

        return count

