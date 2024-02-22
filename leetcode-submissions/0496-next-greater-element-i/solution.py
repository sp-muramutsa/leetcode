class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time O(length_1 * length_2)
        Space O(1)
        """
        length_1 = len(nums1)
        length_2 = len(nums2)

        for i in range(length_1):
            index = nums2.index(nums1[i])
            for j in range(index, length_2):
                flag = 1 # to check swaps
                if nums2[j] > nums1[i]:
                    nums1[i] = nums2[j]
                    flag *= 0 # show that swap was made
                    break # leave the loop imediately since we only want the first greater element
            if flag == 1: # check if a swap was made
                nums1[i] = -1
        
        return nums1


        
        
        
