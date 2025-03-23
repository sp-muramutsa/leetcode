class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums)
        for i in set_nums:
            if (i-1) not in set_nums:
                length = 0
                while (i+length) in set_nums:
                    length += 1
                longest = max(longest, length)
        return longest
