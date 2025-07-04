import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)

            if heaviest != second_heaviest:
                diff = heaviest - second_heaviest
                heapq.heappush(stones, diff)

        if len(stones) == 1:
            result = heapq.heappop(stones)
            return -result
        else:
            return 0

