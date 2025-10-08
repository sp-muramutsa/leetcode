import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = (sum(nums))/2
        nums = [-num for num in nums]
        heapq.heapify(nums)

        answer = 0

        while half > 0:
            largest = heapq.heappop(nums)
            half += (largest/2)
            heapq.heappush(nums, (largest/2))

            answer += 1

        return answer
