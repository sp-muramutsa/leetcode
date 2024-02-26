class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge sort solution
        Time O(nlogn)
        """

        """
        If only one number
           Quit
        Else
            Sort left half of number
            Sort right half of number
            Merge sorted halves
        """
        length = len(nums)
        
   
                
        # Base case: If only one number, return
        if length <= 1:
            return nums
        
        # Partition
        mid = length // 2
        left = nums[:mid]
        right = nums[mid:]
        
        # Recursion
        self.sortArray(left)
        self.sortArray(right)

        # Merge the sorted arrays
        left_index = 0
        right_index = 0
        merged_index = 0

        length_left = len(left)
        length_right = len(right)

        while left_index < length_left and right_index < length_right:
            
            if left[left_index] < right[right_index]:
                nums[merged_index] = left[left_index]
                left_index += 1
                
            
            else:
                nums[merged_index] = right[right_index]
                right_index += 1
            
            merged_index += 1
        
        while left_index < length_left:
            nums[merged_index] = left[left_index]
            left_index += 1
            merged_index += 1
        
        while right_index < length_right:
            nums[merged_index] = right[right_index]
            right_index += 1
            merged_index += 1
        
        return nums
    




         




