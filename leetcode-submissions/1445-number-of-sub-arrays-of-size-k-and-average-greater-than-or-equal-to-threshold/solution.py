class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Time: O(n)
        Space: O(1)
        Intuition: Slide a window of size k through the array while calculating the average of that window. If the average is >= threshold, count it. 
        """

        def is_valid(current_sum):
            return (current_sum / k) >= threshold   
        
        l, r = 0, k-1
        length = len(arr)
        curr_sum = sum(arr[:r])
        result = 0

        while r < length:
            curr_sum += arr[r]
            if is_valid(curr_sum):
                result += 1
            curr_sum -= arr[l] 
            l += 1
            r += 1
        
        return result
        
            
            


