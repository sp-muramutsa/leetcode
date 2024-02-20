class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        previous = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in previous:
                return [previous[difference], index]
            previous[number] = index
        
        return 

