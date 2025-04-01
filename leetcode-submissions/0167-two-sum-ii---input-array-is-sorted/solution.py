class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #we will use two pointers to solve this problem
        #we set our left and right pointer
        l, r = 0, len(numbers) - 1
        #we iterate through our list
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                return [l+1, r+1]
