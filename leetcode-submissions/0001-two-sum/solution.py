class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        i = 0
        while i < length:
            j = 0
            while j < length:
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        
