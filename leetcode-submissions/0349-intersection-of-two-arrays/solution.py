class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Intuition: Hash one list and iterate another one checking if its elements are in the hashmap
        """
        intersec = set()
        length1 = len(nums1)
        hashmap2 = {}
        for index2, number2 in enumerate(nums2):
            hashmap2[number2] = index2
        

        for number1 in nums1:
            if number1 in hashmap2:
                intersec.add(number1)
        return intersec
