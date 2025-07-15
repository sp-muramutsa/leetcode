class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution= []

        def backtrack(nums_used, path):
            if nums_used == n:
                solution.append(path[:])
                return

            for j in range(n):
                if nums[j] in path:
                    continue
                
                path.append(nums[j])
                backtrack(nums_used + 1, path)
                path.pop()

        backtrack(0, [])
        return solution

