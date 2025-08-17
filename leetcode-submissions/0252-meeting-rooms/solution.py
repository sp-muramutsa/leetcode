class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if not intervals:
            return True

        intervals.sort()
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                return False
            prev_end = end

        return True

