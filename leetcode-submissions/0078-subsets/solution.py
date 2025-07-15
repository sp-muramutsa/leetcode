class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution = []

        def backtrack(i, path):     
            
            solution.append(path[:])
            
            if i == n:
                return
            
            for j in range(i, n):
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()
        
        backtrack(0, [])
        return solution




        
