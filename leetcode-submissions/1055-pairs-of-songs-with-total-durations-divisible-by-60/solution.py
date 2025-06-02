class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        pairs = 0
        n = len(time)

        hashmap = defaultdict(int)
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60 # The % 60 is to handle the case where remainder = 0 i.e. t = 60

            if complement in hashmap:
                pairs += hashmap[complement]
            hashmap[remainder] += 1

        return pairs

