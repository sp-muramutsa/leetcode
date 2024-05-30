class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        """
        Time: O(n)
        Space: O(1)
        Intuition: Start from the end tracking the right maximum value and updating accordingly
        """
       
        i = len(arr) - 1
        right_max = arr[-1]

        while i >= 0:
            temp = arr[i]
            arr[i] = right_max
            right_max = max(right_max, temp)
            i -= 1
        
        # Set the last element to a -1
        arr[-1] = -1
        
        return arr
        
