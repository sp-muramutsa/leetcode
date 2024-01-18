class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for number in nums1:
            for another_number in nums2:
                if number == another_number and number not in intersection:
                    intersection.append(number)
        
        return intersection
        

        
