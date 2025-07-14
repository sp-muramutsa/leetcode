class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution, path = [], []
        nums.sort()

        def backtrack(i, path):
            print(i, path)
            solution.append(path[:])
            if i == n:
                return

            for j in range(i + 1, n):

                # Prune for duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                path.append(nums[j])
                backtrack(j, path)
                path.pop()

        backtrack(-1, path)
        return solution

