class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[n] = i
