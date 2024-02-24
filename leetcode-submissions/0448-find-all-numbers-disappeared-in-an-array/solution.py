class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        """
        Time O(n)
        Space O(n)
        """

        n = len(nums)
        nums = set(nums)
        all_in_range = (i for i in range(1, n + 1))

        return [x for x in all_in_range if x not in nums]

        
