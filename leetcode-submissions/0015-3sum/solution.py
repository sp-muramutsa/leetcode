class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #using set to remove duplicates
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                ans = nums[i] + nums[l] + nums[r]
                if ans < 0:
                    l += 1
                elif ans > 0:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(res)
