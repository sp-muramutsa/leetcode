class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution = []
        visited = {i: False for i in range(n)}
        nums.sort()

        def backtrack(i, path_length, path, visited):
            if path_length == n:
                solution.append(path[:])
                return

            for j in range(n):

                if visited[j]:
                    continue

                if j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]:
                    continue

                path.append(nums[j])
                visited[j] = True
                backtrack(j + 1, path_length + 1, path, visited)
                path.pop()
                visited[j] = False

        backtrack(0, 0, [], visited)
        return solution

