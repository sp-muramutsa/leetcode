from collections import deque
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Starting from position m nums1 
        # Replace the values with nums2 starting from back to n
        # Sort the list
        start = len(nums2) - n
        for i in range(m, len(nums1)):
            nums1[i] = nums2[start]
            start += 1
        nums1.sort()
