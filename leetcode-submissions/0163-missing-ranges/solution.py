class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        
        missing_ranges = []
        # We start by a number higher than lower
        if nums[0] > lower:
            missing_ranges.append([lower, nums[0] - 1])

        # Middle check
        for i in range(n - 1):
            # If there are missing numbers i.e. diff = 0(same nbr) or diff = 1(consecutive)
            if nums[i+1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i] + 1, nums[i+1] -1])
        
        # We start by a number bigger than upper
        if nums[-1] < upper:
            nums.append(upper + 1)
            missing_ranges.append([nums[-2] + 1, upper])

        return missing_ranges





        
