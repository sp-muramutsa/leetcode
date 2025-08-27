class Solution:
    def rob(self, nums: List[int]) -> int:

        # Exculde first house
        n = len(nums)

        if n == 1:
            return nums[0]

        elif n == 2:
            return max(nums[0], nums[1])

        a = nums[1]
        b = max(nums[1], nums[2])
        temp = b

        for i in range(3, n):
            temp = max(a + nums[i], b)
            a = b
            b = temp

        answer1 = temp

        # Exclude last house
        a = nums[0]
        b = max(nums[0], nums[1])
        temp = b

        for i in range(2, n - 1):
            temp = max(a + nums[i], b)
            a = b
            b = temp

        answer2 = temp

        return max(answer1, answer2)

