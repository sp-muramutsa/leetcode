class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        length = len(nums)

        for index, number in enumerate(nums):
            hashmap[number] = index  

        for i in range(length):
            complement = target - nums[i]
            if complement in hashmap and i != hashmap[complement]:
                return [hashmap[complement], i]



