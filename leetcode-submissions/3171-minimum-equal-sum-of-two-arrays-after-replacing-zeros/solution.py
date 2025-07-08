class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        countZeros1 = nums1.count(0)
        countZeros2 = nums2.count(0)

        sum1 = sum(nums1) + countZeros1
        sum2 = sum(nums2) + countZeros2

        if sum1 == sum2:
            return sum1 

        if sum1 < sum2 and countZeros1 > 0:
            return sum2

        if sum1 > sum2 and countZeros2 > 0:
            return sum1

        return -1

