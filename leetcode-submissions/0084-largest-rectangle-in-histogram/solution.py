class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        stack = []
        max_area = 0

        # First Pass
        for i in range(n):
            prev = i
            while stack and heights[i] < stack[-1][0]:
                    height, index =  stack.pop()
                    width = i - index
                    area = height * width
                    max_area = max(max_area, area)
                    prev = index  # Index to which this bar(heights[i]) can extend backwards up to   
            
            stack.append((heights[i], prev))
           
        

        # Second Pass: Emptying the stack. n is an imaginary bar.
        while stack:
            height, index = stack.pop()
            width = n - index
            area = height * width
            max_area = max(area, max_area)

        return max_area

