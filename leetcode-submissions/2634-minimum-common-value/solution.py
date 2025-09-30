class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first_set = set(nums1)
        second_set = set(nums2)

        common_set = first_set & second_set

        if len(common_set) >= 1:
            return min(common_set)
        else:
            return -1
        
