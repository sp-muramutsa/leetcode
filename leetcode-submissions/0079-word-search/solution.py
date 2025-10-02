class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Every cell can be a source
        # DFS with tracking the word

        # DFS
        # Goal state
        # path_len == n
        # Fail state
        # all possible cells from source visited

        n = len(word)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, i, visited):

            if i == n - 1:
                return True

            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == word[i + 1]:
                    if (nr, nc) in visited:
                        continue

                    if dfs(nr, nc, i + 1, visited):
                        return True

            visited.remove((row, col))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False

