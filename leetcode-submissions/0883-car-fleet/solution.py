class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        position = sorted(cars, key=lambda x: x[0], reverse=True)


        stack = []

        for d, s in position:
            time = (target - d) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)
