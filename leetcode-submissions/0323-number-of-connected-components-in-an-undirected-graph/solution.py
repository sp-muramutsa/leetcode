from collections import deque
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 1
        
        graph = defaultdict(list)
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
            
        visited = set()
        answer = n - len(graph)
        
        def bfs(node):
            visited.add(node)
            queue = deque([node])
            
            while queue:
                current_node = queue.popleft()
                
                for neighbour in graph[current_node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        
        for node in graph:
            if node not in visited:
                answer += 1
                bfs(node)
        return answer
