class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(1)
        Intuition: We know the array must be either increasing or decreasing monotonic so we make a loop that checks both at the same time.
        """

        length = len(nums) 
        increase, decrease = True, True

        for i in range(1, length):
            # Assuming monotonic increase
            if nums[i - 1] > nums[i]:
                increase = False
            
            # Assuming monotonic decrease
            if nums[i - 1] < nums[i]:
                decrease = False
        
        return increase or decrease # If both are none then it's not monotonic at all
                




        
