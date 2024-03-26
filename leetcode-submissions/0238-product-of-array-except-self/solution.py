class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        Time O(n)
        Space O(n)
        """

        l_mult, r_mult = 1, 1
        length = len(nums)
        left, right = [0] * length, [0] * length

        for i in range(length):
            j = -i- 1
            left[i], right[j] = l_mult, r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [a * b for a, b in zip(left, right)]

        
        


        
        
