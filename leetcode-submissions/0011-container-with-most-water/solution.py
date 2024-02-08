class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right, ans = 0, len(height) - 1, 0

        while left < right:
            current_ans = (right - left) * min(height[left], height[right])
            ans = max(current_ans, ans)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans

            
        
