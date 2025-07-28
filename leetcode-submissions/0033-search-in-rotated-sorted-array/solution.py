class Solution:

    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # Left sorted subarray
            elif nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            # Right sorted
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid

        return l if nums[l] == target else -1

