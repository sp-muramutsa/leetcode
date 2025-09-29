"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if node is None:
            return

        hashmap = defaultdict(list)
        visited = set()

        def dfs(node):

            clone_node = Node(node.val)
            hashmap[node] = clone_node
            visited.add(node)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    clone_neighbor = dfs(neighbor)
                    clone_node.neighbors.append(clone_neighbor)
                else:
                    clone_node.neighbors.append(hashmap[neighbor])

            return clone_node

        dfs(node)
        return hashmap[node]

