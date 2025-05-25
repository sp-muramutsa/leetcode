class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]  # Fast goes twice as slow
            if slow == fast:  # Found an intersection
                break

        # Now take slow back to the start and move both pointers at the same pace of +1
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

