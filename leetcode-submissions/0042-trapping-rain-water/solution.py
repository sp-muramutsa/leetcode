class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0
        max_l, max_r = 0, 0
        while l < r:
            if height[l] < height[r]:
                diff = max_l - height[l]
                if diff > 0:
                    water += diff
                max_l = max(max_l, height[l])
                l += 1
            else:
                diff = max_r - height[r]
                if diff > 0:
                    water += diff
                max_r = max(max_r, height[r])
                r -= 1
        return water
