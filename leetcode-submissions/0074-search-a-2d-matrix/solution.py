class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m

        while l < r:
            m = (l + r) // 2

            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if matrix[m][mid] == target:
                    return True
                elif matrix[m][mid] > target:
                    right = mid
                else:
                    left = mid + 1

            if matrix[m][0] > target:
                r = m
            elif matrix[m][0] < target:
                l = m + 1
            else:
                return True


        return False

