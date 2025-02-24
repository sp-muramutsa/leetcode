class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        max_left, max_right = height[l], height[r]

        water = 0
        while l < r:
            if (
                max_left < max_right
            ):  # Move the minimum one: This mirrors the behavior of min(max_left, max_right) that the O(n) space solution was using.
                l += 1
                max_left = max(max_left, height[l])
                water += (
                    max_left - height[l]
                )  # Pay attention how this can never be negative because we updated max_left first

            else:
                r -= 1
                max_right = max(max_right, height[r])
                water += max_right - height[r]  # Idem au max_left

        return water

