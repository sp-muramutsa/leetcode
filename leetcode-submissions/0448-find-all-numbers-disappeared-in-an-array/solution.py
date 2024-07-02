class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        Intuition: We'll mark the presence of each number in the list by negating the value at the index corresponding to each number (adjusted for 0-based indexing). By iterating through the list, for each number 'number', we mark 'nums[abs(number) - 1]' as negative. After this marking step, any index that remains positive indicates that the number 'index + 1' is missing from the list. This allows us to find all missing numbers while only modifying the input list and using constant extra space.
        """
        n = len(nums)

        for number in nums:
            number = abs(number)
            nums[number - 1] = -abs(nums[number - 1])

        result = []
        for index, num in enumerate(nums):
            if num > 0:
                result.append(index + 1)

        return result

