class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # Monotonic Stack Solution: Time Complexity -> O(n)
        n = len(temperatures)
        answer = [0] * n
        stack = [] # pair: day -> temperature
        
        
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        
        return answer
        
