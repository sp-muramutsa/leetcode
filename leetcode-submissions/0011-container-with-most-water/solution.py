class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        area, max_area = 0, 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

