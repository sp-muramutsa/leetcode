class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        length = len(numbers)
        l, r = 0, length - 1

        while  l < r:
            # solution
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

            # right
            elif numbers[l] + numbers[r] > target:
                r -= 1
            
            # left
            elif numbers[l] + numbers[r] < target:
                l += 1
