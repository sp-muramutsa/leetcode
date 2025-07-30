class Solution:
    def can_distribute(self, k, quantities, n):
        """
        n = 6, quantities = [11, 6]
        - the max any store can get is max(quantities)
        - the min any store can get is 0

        - 0 to 11
        - We can only send products to 2 stores since we have 2 product types.

        - max amount -> can be distributed?       n(11) splits. n(6) splits
        - 11    -> yes                            0             0.
        - 10: 1, 10 -> Yes                        1             0
        - 9: 2, 9 -> Yes                          1             0
        - 8: 3, 8 -> Yes                          1             0
        - 7: 4, 7 -> Yes                          1             0
        - 6: 5, 6 -> Yes                          1.            0
        - 5: 5, 6 -> 5, 5, 1 -> Yes               2             1      5, 1
        - 4: 4, 7 -> 4, 4, 3 -> Yes               2             1      4, 2
        - 3: 3, 8 -> 3, 3, 5-> 3, 3, 3, 2 -> Yes.       3      1      3, 3
        - 2: 2, 9 -> 2, 2, 7 -> 2, 2, 2, 5 -> 2, 2, 2, 2, 3 -> 2, 2, 2, 2, 2, 1 -> 5.     2 2, 2, 2
        - 1: ... -> 10 times, 5 times
        - Formula = (x - 1) // y ... operations to divide x into y parts

        15, 7, 4, 3, 3, 1, 1, 1, 1, 1, 0

        0, 1, 1, 1, 1, 1, 3, 3, 4, 7, 15

        last one to be less than n
        """

        num_stores = 0
        for qty in quantities:
            num_stores += ceil(qty / k)
        return num_stores <= n

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        l, r = 1, max(quantities)

        while l < r:
            mid = l + (r - l) // 2

            if self.can_distribute(mid, quantities, n):
                r = mid
            else:
                l = mid + 1

        return l

