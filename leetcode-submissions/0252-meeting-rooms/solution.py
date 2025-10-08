class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if not intervals:
            return True

        intervals.sort()
        last = intervals[0]

        for interval in intervals[1:]:
            if interval[0] < last[1]:
                return False
            last = interval
        
        return True
