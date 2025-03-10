class Solution:
    # O(log(m * n))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        U, D = 0, n - 1

        # Up and Down
        while U <= D:
            MID = U + (D - U) // 2
            if self.binary_search(MID, matrix, target):
                return True

            if matrix[MID][-1] < target:
                U = MID + 1

            elif matrix[MID][-1] > target:
                D = MID - 1

        return False

    # Right to Left in a Row
    def binary_search(self, MID, matrix, target):
        print(matrix[MID])
        l, r = 0, len(matrix[MID]) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if matrix[MID][mid] == target:
                return True

            elif matrix[MID][mid] > target:
                r = mid - 1

            elif matrix[MID][mid] < target:
                l = mid + 1

        return False

