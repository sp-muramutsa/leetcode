class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        
        for j in range(k, len(nums)):
            if dq and dq[0] == j - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            dq.append(j)
            res.append(nums[dq[0]])
        return res
    
                
        
