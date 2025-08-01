class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            curr_area = h * w
            area = max(curr_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area
