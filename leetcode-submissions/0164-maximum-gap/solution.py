class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = len(nums)
        maximum = max(nums)
        minimum = min(nums)
        if minimum - maximum == 0:
            return 0
        size = (maximum-minimum)/length
        bucket = [[] for i in range(length+1)]
        for i in nums:
            position = int((i-minimum)//size)
            bucket[position].append(i)
        res = []
        for i in bucket:
            sub = sorted(i)
            res += sub
        result = 0
        for i in range(1, len(res)):
            result = max(result, res[i]-res[i-1])
        return result
