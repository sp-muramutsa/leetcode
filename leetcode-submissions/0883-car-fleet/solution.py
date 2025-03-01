class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 

        n = len(position)
        position_speed = [(position[i], speed[i]) for i in range(n)]
        position_speed.sort()
        time = [(target-position_speed[i][0]) / position_speed[i][1] for i in range(n)]
        time = list(reversed(time))

        stack = []
        for t in time:
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        
        
            
        
