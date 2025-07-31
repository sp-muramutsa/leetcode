class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l, r = 0, n - 1

        while l < r:

            mid = l + (r - l) // 2

            # Left sorted part
            if nums[mid] > nums[r]:
                # Check if target lies in the left sorted part
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            # Right sorted part
            elif nums[mid] < nums[r]:
                # Check if target lies in the right sorted part
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

            else:
                r -= 1

        return nums[l] == target

