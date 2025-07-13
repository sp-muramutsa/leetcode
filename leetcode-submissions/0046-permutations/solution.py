class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution, path = [], []

        def backtrack(i):
            if len(path) == n:
                solution.append(path.copy())
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(num)
                    path.pop()

        backtrack(1)
        return solution

