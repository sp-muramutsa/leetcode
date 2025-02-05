class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        heapq.heapify(nums)
        n = len(nums)
        sorted_list = []
        for i in range(n):
            minn = heapq.heappop(nums)
            sorted_list.append(minn)
        
        return sorted_list
