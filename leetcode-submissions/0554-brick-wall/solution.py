class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        #We create a hashmap and add one element just in case the bricks are of sam size and fill both ends, well the idea bhind is that we will create a hashmap and keep the key as the position and value as the number of slices at that position, later we will find the number of cut bricks by len(wall) - slices.
        hashmap = {0 : 0}
        for i in wall:
            position = 0
            for j in i[:-1]:
                position += j
                hashmap[position] = hashmap.get(position, 0) + 1
        slices = max(hashmap.values())
        return len(wall) - slices

