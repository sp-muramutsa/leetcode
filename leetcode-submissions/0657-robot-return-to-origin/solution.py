class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_moves = 0
        y_moves = 0

        number_of_moves = len(moves)
        for i in range(number_of_moves):
            if moves[i] == "R":
                x_moves += 1
            elif moves[i] == "L":
                x_moves -= 1
            elif moves[i] == "U":
                y_moves += 1
            elif moves[i] == "D":
                y_moves -= 1
        
        if x_moves == 0 and y_moves == 0:
            return True
        return False
        
