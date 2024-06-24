class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 
        Time: O(length1 + length2) i.e. O(n)
        Space: O(n)
        Intuition: Iterate from left to right while stacking elements from nums2. Check and see if the current element is greater than what's on the top of the stack, we hash whatever is on the top with that number and keep popping while doing the same(this is where the sugar is. it means that number(from nums2) is the next greater element of the ones we are popping). After we are done iterating, we hash the remaining elements with -1(i.e. they have no next greater element).
        The hardest part is over, now we go in the hashmap to look for the numbers in nums1 and their next elements.
        """
        length2 = len(nums2)
        stack = []
        hashmap = {}

        for i in range(length2):
            while stack and nums2[i] > stack[-1]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            hashmap[stack.pop()] = -1

        length1 = len(nums1)

        for i in range(length1):
            nums1[i] = hashmap[nums1[i]]

        return nums1

