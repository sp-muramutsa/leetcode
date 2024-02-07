from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities_count = len(isConnected)
        cities = {}

        i = len(isConnected)
        j = len(isConnected[0])

        # map a city to direct connections(neighbors)
        for x in range(i):
            for y in range(j):
                if isConnected[x][y] == 1:
                    if x not in cities:
                        cities[x] = [y]
                    else:
                        cities[x].append(y)
        
        # DFS to find connected components
        visited = set()
        def dfs(city):
            visited.add(city)
            if city in cities:
                for neighbor in cities[city]:
                    if neighbor not in visited:
                        dfs(neighbor)
            
           
        
        connected_components = 0
        # Iterate through cities and perform DFS
        for city in range(cities_count):
            if city not in visited:
                dfs(city)
                connected_components += 1

        return connected_components

        
