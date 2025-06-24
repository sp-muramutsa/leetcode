from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque() # Will store indices
        result = []
        n = len(nums)

        # Make the first window
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        
        result.append(nums[dq[0]]) # First window max

        # Other windows
        for j in range(k, n): 
            if j - dq[0] == k:
                dq.popleft()

            while dq and nums[j] > nums[dq[-1]]:
                dq.pop()
          
            dq.append(j)
            result.append(nums[dq[0]])
        
        return result

          
