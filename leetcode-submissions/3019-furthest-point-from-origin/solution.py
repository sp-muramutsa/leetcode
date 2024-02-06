class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        number_of_moves = len(moves)
        lefts = 0
        rights = 0
        underscores = 0

        for i in range(number_of_moves):
            if moves[i] == "L":
                lefts += 1
            elif moves[i] == "R":
                rights += 1
            elif moves[i] == "_":
                underscores += 1
        
        if lefts > rights:
            furthest_distance = lefts + underscores - rights
        else:
            furthest_distance = rights + underscores - lefts
        
        return furthest_distance

        

        
        
