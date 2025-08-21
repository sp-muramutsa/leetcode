"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return 
        visited = set()
        hashmap = {}

        def get_neighbors(node):
            return node.neighbors

        def dfs(node):
            stack = [node]
            hashmap[node] = Node(node.val)
            visited.add(node)

            while stack:
                n = stack.pop()
                for neighbor in get_neighbors(n):
                    if neighbor not in hashmap:
                        hashmap[neighbor] = Node(neighbor.val)
                    hashmap[n].neighbors.append(hashmap[neighbor])
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    stack.append(neighbor)

        dfs(node)
        return hashmap[node]
