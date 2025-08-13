class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROWS, COLS = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        init_color = image[sr][sc]
        stack = deque([(sr, sc)])

        # Iterative DFS
        while stack:

            row, col = stack.pop()

            image[row][col] = color

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if image[nr][nc] == init_color and image[nr][nc] != color:
                    stack.append((nr, nc))

        return image

       
