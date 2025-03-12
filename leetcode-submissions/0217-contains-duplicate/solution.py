class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter:
            if counter[i] > 1:
                return True
        return False
        
