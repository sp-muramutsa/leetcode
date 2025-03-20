class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            digit = target - num
            if digit in hashmap:
                return [hashmap[digit], index]
            hashmap[num] = index
        return -1
