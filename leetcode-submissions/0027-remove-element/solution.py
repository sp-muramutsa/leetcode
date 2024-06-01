class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        """
        Two pointer solution
        The tripping solution was returning the wrong k!!!!!
        """

        length = len(nums)
        l, r = 0, length - 1
        while l < r:
            if nums[l] == val and nums[r] == val:
                nums[r] = val
                r -= 1
 
            
            elif nums[l] == val and nums[r] != val:
                nums[l] = nums[r]
                nums[r] = val
                l += 1
       
            
            elif nums[l] != val:
                l += 1

        x = 0
        for j in range(length - 1, -1, -1):
            if nums[j] == val:
                x += 1
                nums[j] = "_"
            else:
                break

        k = length - x
        return k
