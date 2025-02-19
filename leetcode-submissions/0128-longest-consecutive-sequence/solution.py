class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence, current_sequence = 0, 0

        for number in nums:
            if number - 1 not in nums:
                current_sequence = 1
                while number + 1 in nums:
                    number = number + 1
                    current_sequence += 1

            elif number + 1 not in nums:
                current_sequence = 1
                while number + 1 in nums:
                    number = number + 1
                    current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

