class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [0]*n
        for i in range(n):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    ans[i] = j
        return ans
        
