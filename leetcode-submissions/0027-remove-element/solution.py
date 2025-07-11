class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # A pointer p1 to keep track of the indices to insert in: l
        # A pointer p2 to keep track of the candidates: r
        # Iterate while r < n:
        #   if nums[l] == val:
        # while nums[r] == val:
        # r += 1
        # nums[l] = nums[r]
        # nums[r] = val
        # l += 1
        # r += 1
        #   else:
        #       l += 1
        #       r += 1

        # [0, 1, 2, 2, 3, 0, 4, 2]
        # [0, 1, 3, 2, 2, 0, 4, 2]
        # [0, 1, 3, 0, 2, 2, 4, 2]
        # [0, 1, 3, 0, 4, 2, 2, 2]
        #                 l,    r
        # return l + 1

        n = len(nums)
        if n == 1:
            if val == nums[0]:
                return 0
            else:
                return 1

        l, r = 0, 0

        while r < n:
            if nums[l] == val:
                if nums[r] == val:
                    r += 1

                else:
                    nums[l] = nums[r]
                    nums[r] = val
                    l += 1
                    r += 1

            else:
                l += 1
                r += 1

        return l

