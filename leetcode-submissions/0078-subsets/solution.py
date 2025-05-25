class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def solve(l):
            if l >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[l])
            solve(l+1)
            curr.pop()
            solve(l+1)
        solve(0)
        return res
