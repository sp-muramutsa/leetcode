class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for i in nums_set:
            if (i-1) not in nums_set:
                length = 0
                while (i+length) in nums_set:
                    length += 1
                longest = max(longest, length)

        return longest
