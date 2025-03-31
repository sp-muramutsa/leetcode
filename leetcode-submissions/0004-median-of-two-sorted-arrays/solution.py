class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A  # Ensure A is the smaller array

        l, r = 0, len(A) - 1

        while True:
            mid1 = (l + r) // 2  # A
            mid2 = half - mid1 - 2  # B

            ALeft = A[mid1] if mid1 >= 0 else float("-infinity")
            ARight = A[mid1 + 1] if mid1 + 1 < len(A) else float("infinity")

            BLeft = B[mid2] if mid2 >= 0 else float("-infinity")
            BRight = B[mid2 + 1] if mid2 + 1 < len(B) else float("infinity")

            # Partition is correct
            if ALeft <= BRight and BLeft <= ARight:
                # Odd
                if total % 2 == 0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                # Even
                else:
                    return min(ARight, BRight)

            elif ALeft > BRight:
                r = mid1 - 1
            else:
                l = mid1 + 1

