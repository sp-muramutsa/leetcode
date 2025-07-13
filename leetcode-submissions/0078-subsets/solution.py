class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        solution, path = [], []

        def backtrack(i):
           
            if i == n:
                solution.append(path.copy())
                return
            
            # Don't pick nums[i+1]
            backtrack(i + 1)

            # Pick nums[i]
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
        
        backtrack(0)

        # Time: O(2 ** n)
        # Space: space for the answer. O(2 ** n)
        # Recursion depth space: O(n )

        return solution




        
