class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        
        Intuition: The amount of water trapped at any given position depends on the minimum of the maximum heights 
        to its left and right. Instead of using extra space to store these maximum heights, we can use two pointers 
        to traverse the height array from both ends towards the center. By maintaining the maximum heights encountered 
        so far from both the left and the right, we can directly compute the trapped water.

        1. Initialize two pointers, `l` and `r`, pointing to the beginning and end of the height array, respectively.
        2. Initialize `max_left` and `max_right` to keep track of the maximum heights encountered so far from the left 
           and right.
        3. Traverse the array using the two pointers:
           - If `max_left` is less than `max_right`, move the left pointer (`l`) one step to the right, update `max_left`, 
             and calculate the water trapped at the new position.
           - Otherwise, move the right pointer (`r`) one step to the left, update `max_right`, and calculate the water 
             trapped at the new position.
        4. Continue this process until the two pointers meet.
        5. The total trapped water is the sum of the water trapped at each position.
        """

        length = len(height)
        if length == 0:
            return 0
        
        l, r = 0, length - 1
        max_left, max_right = height[l], height[r]

        trapped = 0
        while l < r:
            if max_left < max_right: # We move the minimum one
                l += 1
                max_left = max(max_left, height[l]) 
                trapped += max_left - height[l] # Don't need to check if it's negative
            else:
                r -= 1
                max_right = max(max_right, height[r])
                trapped += max_right - height[r] # Don't need to check if it's negative
        
        return trapped

            

