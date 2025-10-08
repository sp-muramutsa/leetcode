import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        heapq.heapify(nums)
        answer = 0

        while nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            
            heapq.heappush(nums, (min(first,second) * 2 + max(first, second)))
            answer += 1

        return answer
