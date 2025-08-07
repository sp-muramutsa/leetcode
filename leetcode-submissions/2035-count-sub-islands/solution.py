class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m, n = len(grid2), len(grid2[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = set()

        def dfs(row, col):
            if grid2[row][col] == 1 and grid1[row][col] != 1:
                nonlocal is_island
                is_island = False
            
            visited.add((row, col))
            for dx, dy in directions:
                x, y = row + dx, col + dy
                if 0 <= x < m and 0 <= y < n \
                    and grid2[x][y] == 1 \
                    and (x, y) not in visited:
                    dfs(x, y)
        
        valid_sub_islands = 0
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and (row, col) not in visited:
                    is_island = True
                    dfs(row, col)
                    if is_island:
                        valid_sub_islands += 1
        
        return valid_sub_islands 
                    
                    
