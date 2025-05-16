class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        length = len(nums)
        for key, value in counter.items():
            if value > length/2:
                return key
