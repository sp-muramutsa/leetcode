class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        O(nlogn) - 
        """
        
        left, right = 0, len(arr) -1

        while left <= right:
            pivot = left + (right - left) // 2

            if arr[pivot] - pivot - 1< k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return left + k
            
        
            


        
    




        
        
