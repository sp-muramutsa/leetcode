class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, starting_index):
            res.append(path.copy())

            for i in range(starting_index, len(nums)):
                path.append(nums[i])
                dfs(path, i+1)
                path.pop()

        dfs([], 0)
        return res
