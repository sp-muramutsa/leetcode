from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        dq = deque()
        output = []

        # Part 1: First window max
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        output.append(nums[dq[0]])  # first window max

        # Part 2: After the first window max
        for j in range(k, n):
            # Check if the window is valid
            if dq and j - dq[0] == k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            dq.append(j)
            output.append(nums[dq[0]])

        return output

