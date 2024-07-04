class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negative, positive, ans = nums[0], nums[0], nums[0]
        length = len(nums)
        for i in range(1, length):
            temp = max(nums[i], positive * nums[i], negative * nums[i])
            negative = min(nums[i], negative*nums[i], positive*nums[i])
            positive = temp
            ans = max(ans, positive)

        return ans
            

