from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        result = []
        n = len(nums)

        for i in range(n):

            if dq and i - dq[0] >= k:
                dq.popleft()

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

