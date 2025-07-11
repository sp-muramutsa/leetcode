class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Input: nums = [1,2,3,4]
        # Output: [24,12,8,6]

        # L: [1, 1, 2, 6]
        # R: [24, 12, 4, 1]
        # O: [24, 12, 8, 6]

        n = len(nums)
        L = [1] * n
        L[0] = 1

        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]

        R = [1] * n
        R[n - 1] = 1

        for j in range(n - 2, -1, -1):
            print(j, j + 1)
            R[j] = nums[j + 1] * R[j + 1]

        result = [x * y for (x, y) in zip(L, R)]

        return result

