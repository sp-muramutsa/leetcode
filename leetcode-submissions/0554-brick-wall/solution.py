class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hashmap = {}
        for i in wall:
            count = 0
            for j in i[:-1]:
                count += j
                hashmap[count] = hashmap.get(count, 0) + 1
        val = 0
        for value in hashmap.values():
            val = max(val,value)
        return (len(wall) - val)
