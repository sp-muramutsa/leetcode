class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time: O()
        Space: O(1)
        Intuition: Start from the third element comparing each element with the second element to its left. If they are equal, that means we have more than three instances of the same integer: delete the one on the right. If not, then move by a step and continue the comparisons.
        """
        i, k = 2, len(nums)

        while i < len(nums):
            if nums[i] == nums[i - 2]:
                nums.pop(i)  # pop, remove, and del can all work here
                k -= 1
            else:
                i += 1

        return k

