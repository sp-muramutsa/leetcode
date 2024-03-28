class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        i = 0
        j = 0
        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                pass
            else:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            i += 1    

        # Fill out the remaining zeros
        if 0 in nums1:
            remainder = n-j
            if remainder > 0:
                nums1[-remainder:] = nums2[-remainder:]
        
