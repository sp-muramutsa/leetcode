class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        res = []
        
        for i in nums2:
            if i in count1 and count1[i] > 0:
                count1[i] -= 1
                res.append(i)

        return res
