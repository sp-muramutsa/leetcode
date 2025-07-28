class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        n1, n2 = len(A), len(B)
        total = n1 + n2
        half = total // 2

        lA, rA = 0, n1 - 1

        while True:

            mA = lA + (rA - lA) // 2
            mB = half - mA - 2

            midA = A[mA] if mA >= 0 else float("-inf")
            post_midA = A[mA + 1] if (mA + 1) < n1 else float("inf")

            midB = B[mB] if 0 <= mB else float("-inf")
            post_midB = B[mB + 1] if (mB + 1) < n2 else float("inf")

            if midA <= post_midB and midB <= post_midA:
                # Even
                if total % 2 == 0:
                    left = max(midA, midB)
                    right = min(post_midA, post_midB)

                    return (left + right) / 2

                # Odd
                else:
                    return min(post_midA, post_midB)

            elif midA > post_midB:
                rA = mA - 1

            else:
                lA = mA + 1

