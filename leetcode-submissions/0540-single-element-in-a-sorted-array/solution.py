class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        Intuition: Use binary search to reduce search space by O(logn). The secret sauce here is that the first and last element of the duplicated numbers are positioned in different ways on left vs right of the single element. e.g. if the single is at index 2: we have 0, 1 vs 3, 4. EVEN-ODD vs ODD-EVEN.
        """
        n = len(nums)
        l, r = 0, n-1

        if n == 1:
            return nums[0]

        while l <= r:
            mid = l + (r - l) // 2

            if l == r:
                return nums[l]
            

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            # Right
            elif (mid % 2 == 0 and nums[mid] == nums[mid-1]) or (mid % 2 != 0 and nums[mid] == nums[mid+1]):
                r = mid - 1
            
            # Left
            elif (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 != 0 and nums[mid] == nums[mid-1]):
                l = mid + 1
            
        
        return 0
