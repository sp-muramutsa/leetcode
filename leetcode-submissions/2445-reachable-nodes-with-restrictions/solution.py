from collections import deque, defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        if not edges:
            return 0
        
        graph = defaultdict(list)
        valid_seen = set()
        restricted_set = set(restricted)
        
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
            
        def bfs(node):
            queue = deque([node])
            
            while queue:
                current_node = queue.popleft()
                valid_seen.add(current_node)
                
                for neighbour in graph[current_node]:
                    if (neighbour not in restricted_set) and (neighbour not in valid_seen):
                        queue.append(neighbour)
                        
        bfs(0)
        return len(valid_seen)
