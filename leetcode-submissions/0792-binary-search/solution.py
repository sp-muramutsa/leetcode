class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftmost = 0
        rightmost = len(nums) - 1

        while leftmost <= rightmost:
            middle = (leftmost + rightmost) // 2
            if nums[middle] == target:
                return middle 


            # left side
            elif nums[middle] < target:
                leftmost = middle + 1

            # right side
            elif nums[middle] > target:
                rightmost = middle - 1

        return -1
        
