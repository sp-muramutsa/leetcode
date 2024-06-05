class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        Intuition:
        The algorithm uses the Boyer-Moore Voting Algorithm to find the majority element, which is an element that appears more than half the time in the list.
        - Initialize a counter and a majority candidate.
        - Iterate through the list:
            - If the counter is zero, set the current element as the majority candidate.
            - If the current element is the same as the majority candidate, increment the counter.
            - If the current element is different, decrement the counter.
        - The majority candidate at the end of the iteration is the majority element because it appears more than half the time in the list.
        """

        count, majority = 0, 0

        for number in nums:
            if count == 0:
                majority = number

            count += 1 if number == majority else -1

        return majority

