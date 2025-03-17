class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0

        if (n1 + n2) % 2 == 0:  # Even
            range_of_iteration = (n1 + n2) // 2
            for i in range(range_of_iteration):
                median1, p1, p2 = self.get_min(nums1, nums2, p1, p2, n1, n2)
            median2, p1, p2 = self.get_min(nums1, nums2, p1, p2, n1, n2)
            median = (median1 + median2) / 2

        else:  # Odd
            range_of_iteration = ((n1 + n2) // 2) + 1
            for i in range(range_of_iteration):
                median, p1, p2 = self.get_min(nums1, nums2, p1, p2, n1, n2)

        return median

    def get_min(self, nums1, nums2, p1, p2, n1, n2):
        if p1 < n1 and p2 < n2:
            if nums1[p1] <= nums2[p2]:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1

        elif p1 == n1:
            ans = nums2[p2]
            p2 += 1

        elif p2 == n2:
            ans = nums1[p1]
            p1 += 1

        return ans, p1, p2

