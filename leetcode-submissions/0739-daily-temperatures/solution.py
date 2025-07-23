class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []
        res = [0] * n
        i = 0

        while i < n:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)
            i += 1

        return res

