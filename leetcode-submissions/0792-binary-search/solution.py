class Solution:
    # Recursive
    def search(self, nums: List[int], target: int, l: int = 0, r: int = None) -> int:
        if r is None:
            r = len(nums) - 1
            
        if l > r:
            return - 1
        
        mid = l + (r-l) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            return self.search(nums, target, mid + 1, r)
        
        else:
            return self.search(nums, target, l, mid - 1)
    
    
    

        
