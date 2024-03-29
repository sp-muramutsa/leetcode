class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        Time O(n^2)
        Space O(n)
        """

        nums.sort()
        print(nums)
        k = 0
        length = len(nums)
        threesum = []

        while k < length:
            i, j = k + 1, length - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    threesum.append((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1 
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                else:
                    i += 1           
            k += 1
        
        return list(set(threesum))
        
        
