class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0: #O(k)
            nums.insert(0, nums[-1]) # O(n)
            nums.pop() # O(1)
            k -= 1

        """
        Time complexity: O(n * k)
        Space complexity: O(1)
        """
        
