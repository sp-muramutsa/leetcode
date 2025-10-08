class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        - sort by start time
        - last
        """

        intervals.sort()
        heap = [intervals[0][1]]

        for start, end in intervals[1:]:
            # If the start is later than the end of the top meeting, free up a room
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)

