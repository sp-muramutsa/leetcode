class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        length = len(points)

        for i in range(length):
            x_squared = (points[i][0]) ** 2
            y_squared = (points[i][1]) ** 2
            distances[i] = sqrt(x_squared + y_squared)
             
        distances = sorted(distances.items(), key=lambda x:x[1])
        
        closest_distances = []

        for j in range(k):
            index = distances[j][0]
            closest_distances.append(points[index])
        
        return closest_distances


        

        
    

        
