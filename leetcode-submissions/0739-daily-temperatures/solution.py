class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[len(stack) - 1]] < n:
                index = stack.pop() 
                res[index] = i - index
            stack.append(i)
        return res
