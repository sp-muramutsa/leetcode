class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We use a stack to keep track of temperatures
        # We create a result array with zero values
        stack = []
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            if i == 0:
                stack.append(i)
                continue
            
            elif n < temperatures[i-1]:
                stack.append(i)
                continue
            
            while stack and temperatures[stack[-1]] < n:
                print(stack[-1])
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        print(res)
        return res 
