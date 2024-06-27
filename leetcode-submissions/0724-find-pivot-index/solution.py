class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        Intuition: Iterate while hashing each index with its right and left sums. Find an index whose sums are equal.
        """

        left_hash, right_hash = {}, {}
        length = len(nums)
        left_sum, right_sum = 0, 0

        i = 0
        j = length - 1
        while i < length and j >= 0:

            left_hash[i] = left_sum 
            left_sum += nums[i]

            right_hash[j] = right_sum
            right_sum += nums[j]

            i += 1
            j -= 1

        for k in range(length):
            if left_hash[k] == right_hash[k]:
                return k 

        return -1



        

