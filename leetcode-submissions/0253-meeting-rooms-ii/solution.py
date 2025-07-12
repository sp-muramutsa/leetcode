import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        n = len(intervals)
        intervals.sort() # Sort by start time.
        heap = [intervals[0][1]]

        for i in range(1, n):      
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])        
            
        return len(heap)

       

