import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)
        answer = 0

        while len(sticks) > 1:
            smallest = heapq.heappop(sticks)
            second_smallest = heapq.heappop(sticks)

            answer += smallest + second_smallest
            heapq.heappush(sticks, (smallest + second_smallest))
        
        return answer
