class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(A) > len(B):
            B, A = A, B

        lenA, lenB = len(A), len(B)
        total = lenA + lenB
        half = total // 2

        l, r = 0, lenA - 1

        while True:
            mid1 = l + (r - l) // 2
            mid2 = half - mid1 - 2

            AMid = A[mid1] if mid1 >= 0 else float("-inf")
            APostMid = A[mid1 + 1] if (mid1 + 1) < lenA else float("inf")

            BMid = B[mid2] if mid2 >= 0 else float("-inf")
            BPostMid = B[mid2 + 1] if (mid2 + 1) < lenB else float("inf")

            # Correct partition
            if AMid <= BPostMid and BMid <= APostMid:
                # Odd
                if total % 2 == 1:
                    return min(APostMid, BPostMid)
                else:
                    return (max(AMid, BMid) + min(APostMid, BPostMid)) / 2

            # Too many values from A
            elif AMid > BPostMid:
                r = mid1 - 1
            else:
                l = mid1 + 1

