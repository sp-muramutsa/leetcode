import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a min heap and make it a tuple first element in tuple as Euclidian distance
        if not points:
            return []
        heap = []
        for i in points:
            distance = sqrt((i[0]**2) + (i[1]**2))
            heapq.heappush(heap, (distance, i))

        # Create a result list
        result = []
        # Pop from the list in the range k
        i = 0
        while i < k and heap:
            result.append(heapq.heappop(heap)[1])
            i += 1
            
        # Return the result
        return result
