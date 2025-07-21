class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # O(logn)
        # Binary search: Bisection left
        # Is the element is less or equal to the element on its left or the element on its right ?
        # [-inf, 1, 2, 1, 3, 5, 6, 4, -inf]
        # [1, 2, 1, 3, 5, 6, 4, -inf] nums[mid] = 3
        # [5, 6, 4, -inf] l = 5, r = 8, mid = 6
        # [5, 6] l = 5, r = 6, nums[mid] = 5
        # 5 fails the test and l = mid + 1. l = 5
        # [T, F, ]
        # [T, T, T, T, F] -> First False

        # [3, 2, 1]
        # [-inf, 3, 2, 1, -inf] l = 1, r = 4. mid = 2

        # Traditional binary search. Shift it to the direction of the larger element
        # [3,4,3,2,1]
      
    
        n = len(nums)  
        nums = [float("-inf")] + nums + [float("-inf")]

        l, r = 1, n 
        while l < r:    
            
            mid = l + (r - l) // 2
            print(nums[l], nums[mid], nums[r])
            
            if nums[mid - 1] > nums[mid] or nums[mid] < nums[mid + 1]:
                
                # Left
                if nums[mid - 1] < nums[mid + 1]:
                    l = mid + 1
                
                # Right
                else:
                    r = mid
            
            
            else:
                return mid - 1
        
        return l - 1


        


