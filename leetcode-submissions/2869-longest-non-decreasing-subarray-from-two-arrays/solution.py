class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        longest_1, longest_2 = 1, 1
        max_len = 1

        for i in range(1, n):

            new_longest_1, new_longest_2 = 1, 1

            if nums1[i] >= nums1[i - 1]:
                new_longest_1 = max(new_longest_1, longest_1 + 1)

            if nums1[i] >= nums2[i - 1]:
                new_longest_1 = max(new_longest_1, longest_2 + 1)

            if nums2[i] >= nums1[i - 1]:
                new_longest_2 = max(new_longest_2, longest_1 + 1)

            if nums2[i] >= nums2[i - 1]:
                new_longest_2 = max(new_longest_2, longest_2 + 1)

            longest_1, longest_2 = new_longest_1, new_longest_2
            max_len = max(max_len, longest_1, longest_2)

        return max_len

