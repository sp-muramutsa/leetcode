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
            compliment = target - nums[i]
            print(compliment)

            if compliment in hashmap and hashmap[compliment] != i:
                return [hashmap[compliment], i]
            else:
                pass
        return


