class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create a sorted list of heights
        # Iterate over the sorted list if the number doesn't relate to the main one we increament the res 
        ans = 0
        sorted_heights = sorted(heights)
        for i in range(len(sorted_heights)):
            if sorted_heights[i] != heights[i]:
                ans += 1
                
        return ans
