class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """ 
        Time O(n)
        Space O(1)
        """
        
        length = len(nums)
        bigsum = sum(nums)
        leftsum = 0

        for index, number in enumerate(nums):
            if leftsum == (bigsum - leftsum - number):
                return index
            leftsum += number
        return -1
        
