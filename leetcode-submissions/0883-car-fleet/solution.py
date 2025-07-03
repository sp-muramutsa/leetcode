class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        arrival_times = [(target - pos) / speed for pos, speed in cars]

        stack = []

        for t in arrival_times:
            stack.append(t)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)

