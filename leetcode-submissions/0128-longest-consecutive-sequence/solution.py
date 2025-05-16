class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for number in s:
            if (number-1) not in s:
                length = 0
                while (length + number) in s:
                    length += 1
                longest = max(longest, length)
        return longest
       
