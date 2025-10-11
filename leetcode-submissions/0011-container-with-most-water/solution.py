class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0

        while start < end:
            start_line = height[start]
            end_line = height[end]
            smaller = start_line

            if start_line > end_line:
                smaller = end_line

            curr_area = (end - start) * smaller
            if area < curr_area: 
                area = curr_area

            if start_line > end_line:
                end -= 1
            else:
                start += 1

        return area
