class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #We first create our result variable
        res = []
        #As we are doing all possiible permutation we will use backtracking and extract all possible possiblities, and thiis problem doesn't have any constraints.
        def backtracking(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            #Now because we are using permuatation this is where we loop over over our nums.
            for i in nums:
                if i in curr:
                    continue
                curr.append(i)
                backtracking(curr)
                curr.pop()
            #Once the current i reaches the end that means no more number that wasn't iterated over so we backtrack.
            return
        backtracking([])
        return res
