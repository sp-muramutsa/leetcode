class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        q = deque([(sr, sc)])
        original_color = image[sr][sc]
        image[sr][sc] = color
        visited = set()

        while q:

            row, col = q.popleft()
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (nr, nc) in visited:
                    continue

                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image


