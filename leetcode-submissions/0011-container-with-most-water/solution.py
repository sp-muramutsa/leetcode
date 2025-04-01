class Solution:
    def maxArea(self, height: List[int]) -> int:
        #we first set the pointers
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            width = r - l
            curr_height = min(height[l], height[r])
            area = max(area, (width * curr_height))
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                l += 1
        return area
