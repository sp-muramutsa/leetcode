class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #we sort our list
        #we iterrate over the list
        #we check if the first number is less than the previous end number
        #return false if true else True
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
