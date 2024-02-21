class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        """
        Time: O(n) 
        Space O(1) 
        """
        length = len(arr)
        m = arr[-1]
        for i in range(length - 1, -1, -1):
            if arr[i] > m:
                m, arr[i] = arr[i], m
            else:
                arr[i] = m
        arr[-1] = -1

        return arr
        
     

        
        
        
        

        

       

        


    
        
