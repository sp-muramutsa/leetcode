class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        def backtrack(starting_index, path):
            result.append(path.copy())

            if starting_index == length:
                return

            for i in range(starting_index, length):
                if i > starting_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result
