from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Intuition: Sort the lists. Iterate through both lists. If we find a common element we append it to our result. Else we try to shift the pointers for small elements to get compared to high ones.
        """
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        i = j = 0
        result = []

        while i < length1 and j < length2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i]) # or result.append(nums2[j])
                i += 1
                j += 1
        return result

        
    


