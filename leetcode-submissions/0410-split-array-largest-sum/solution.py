class Solution:
    # dynamic programming
    # def splitArray(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     prefixSum = [0] + list(itertools.accumulate(nums))
    #     @functools.lru_cache(None)
    #     def findMaximum(currIndex: int, k: int):
    #         if k == 1:
    #             return prefixSum[n] - prefixSum[currIndex]
    #         ans = prefixSum[n]
    #         for j in range(currIndex, n - k + 1):
    #             firstSum = prefixSum[j + 1] - prefixSum[currIndex]
    #             currMaxSum = max(firstSum, findMaximum(j + 1, k - 1))
    #             ans = min(ans, currMaxSum)
    #             if firstSum >= currMaxSum:
    #                 break
    #         return ans
    #     return findMaximum(0, k)

    #binary search
    def splitArray(self, nums: List[int], k: int) -> int:

        def min_subarrays_required(max_sum_allowed: int) -> int:
            total = 0
            subs = 1

            for num in nums:
                if total + num > max_sum_allowed:
                    subs += 1
                    total = num
                else:
                    total += num
            return subs

        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            print(low, high, mid)
            if min_subarrays_required(mid) <= k:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans









    #when k = 2
    # total = 0
    # for i in range(len(nums)):
    #     total += nums[i]

    # leftSum = 0
    # ans = float(inf)
    # for j in range(len(nums)):
    #     leftSum += nums[j]
    #     rightSum = total - leftSum
    #     maxSum = max(leftSum, rightSum)
    #     ans = min(maxSum, ans)
    # return ans




        
