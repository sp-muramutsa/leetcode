class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        n = len(intervals)
        if n == 1:
            return intervals

        result = []
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(interval[1], result[-1][1])

            else:
                result.append(interval)

        return result

