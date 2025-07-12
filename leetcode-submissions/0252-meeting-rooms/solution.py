class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # Sort meetings by start time
        # Loop through the meetings and make sure that each meeting ends before the next one starts.

        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        for i in range(1, n):
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True

