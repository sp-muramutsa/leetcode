# Brute-force Solution
class Solution: 
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                top = -1 if i == 0 else mat[i-1][j]
                bottom = -1 if i == m-1 else mat[i+1][j]
                left = -1 if j == 0 else mat[i][j-1]
                right = -1 if j == n-1 else mat[i][j+1]
                neighbors = [top, bottom, left, right]
                
                if all(mat[i][j] > neighbor for neighbor in neighbors):
                    return [i, j]
        return []
