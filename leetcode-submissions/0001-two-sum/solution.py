class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        n = len(nums)

        for index, num in enumerate(nums):
            hashmap[num] = index

        for i in range(n):
            diff = target - nums[i]
            if diff in hashmap and i != hashmap[diff]:
                return [i, hashmap[diff]]

       
