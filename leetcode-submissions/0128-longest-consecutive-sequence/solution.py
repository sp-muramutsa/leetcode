class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence, current_sequence = 0, 0
        nums_set = set(nums)
        i, n = 0, len(nums)

        for number in nums_set:
            # Start of a sequence
            if number - 1 not in nums_set:
                current_sequence = 1
                while number + 1 in nums_set:
                    current_sequence += 1
                    number += 1
            
            # End of a sequence
            if number + 1 not in nums_set:
                current_sequence = 1
                while number - 1 in nums_set:
                    current_sequence += 1
                    number -= 1
            longest_sequence = max(longest_sequence, current_sequence)
        
        return longest_sequence
