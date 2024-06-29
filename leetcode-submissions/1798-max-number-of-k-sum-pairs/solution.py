class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        0. get the first number a, look for k-a and remove both of them?
        1. sort then use two pointer

        '''

        nums.sort()
        ans = 0
        front = 0
        end = len(nums) - 1
        while front < end:
            total = nums[front] + nums[end]
            if total == k:
                ans += 1
                front += 1
                end -= 1
            elif total < k:
                front += 1
            else:
                end -= 1
        return ans
        
