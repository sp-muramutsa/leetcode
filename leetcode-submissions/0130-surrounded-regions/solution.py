class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        edges = []
        for i in range(len(board[0])):
            edges.append((0, i))
            edges.append((len(board)-1, i))

        for i in range(1, len(board)-1):
            edges.append((i, 0))
            edges.append((i, len(board[0])-1))

        def get_neighbors(cell, grid):
            new_r = [1, 0, -1, 0]
            new_c = [0, 1, 0, -1]
            moves = []
            for i in range(4):
                r = new_r[i] + cell[0]
                c = new_c[i] + cell[1]
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "O":
                    moves.append((r, c))
            return moves

        visited = set()
        def dfs(cell):
            stack = [cell]
            while stack:
                n = stack.pop()
                if n in visited:
                    continue
                visited.add(n)
                board[n[0]][n[1]] = "S"
                for i in get_neighbors(n, board):
                    if i not in visited:
                        stack.append(i)

        for edge in edges:
            if board[edge[0]][edge[1]] == "O":
                dfs(edge)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

