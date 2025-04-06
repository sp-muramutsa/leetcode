class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = 0  
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i-1])
        
        right_max[n-1] = 0
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
        water = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                water += water_level - height[i]
        
        return water
