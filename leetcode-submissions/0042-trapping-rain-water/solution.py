class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[0], height[len(height) - 1]
        res = 0

        while l < r:
            if height[l] < height[r]:
                diff = max_l - height[l]
                if diff > 0:
                    res += diff
                max_l = max(max_l, height[l])
                l += 1
            
            else:
                diff = max_r - height[r]
                if diff > 0:
                    res += diff
                max_r = max(max_r, height[r])
                r -= 1          

        return res
