class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find the right row
        # leftR, rightR = 0, m

        # midR = leftR + rightR
        # if nums[midR][0] > target:
        # rightR = mid - 1
        # else:
        # if nums[mid][n - 1] < target:
        # leftR = midR + 1
        # else:  --- RIGHT ROW
        # l, r = 0, n
        # while l < r:
        #   tout de suite ...

        m, n = len(matrix), len(matrix[0])

        L, R = 0, m - 1

        while L <= R:

            M = (L + R) // 2

            if matrix[M][0] > target:
                R = M - 1
            else:
                if matrix[M][n - 1] < target:
                    L = M + 1
                else:

                    left, right = 0, n - 1
                    while left <= right:

                        mid = (left + right) // 2

                        if matrix[M][mid] == target:
                            return True
                        elif matrix[M][mid] < target:
                            left = mid + 1
                        else:
                            right = mid - 1
                    break

        return False

