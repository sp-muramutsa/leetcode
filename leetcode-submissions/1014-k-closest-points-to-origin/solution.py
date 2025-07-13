class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []
        for point in points:
            x, y = point
            distance_to_origin = sqrt(x**2 + y**2)

            heapq.heappush(max_heap, (-distance_to_origin, point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        k_th_closest_points = [point for dist, point in max_heap]
        return k_th_closest_points

