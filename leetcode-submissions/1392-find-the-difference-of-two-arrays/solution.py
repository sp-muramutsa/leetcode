class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        result = [[], []]

        for number in nums1_set:
            if number not in nums2_set:
                result[0].append(number)
        
        for number in nums2_set:
            if number not in nums1_set:
                result[1].append(number)
        
        return result
        
        
