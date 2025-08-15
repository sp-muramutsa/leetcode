class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(1, n + 1)}
        self.ranks = {i: 0 for i in range(1, n + 1)}
        self.components = n

    def find(self, x):

        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):

        parent_x, parent_y = self.find(x), self.find(y)

        if parent_x == parent_y:
            return

        rank_x, rank_y = self.ranks[x], self.ranks[y]

        if rank_x > rank_y:
            self.parents[parent_y] = parent_x
        elif rank_y > rank_x:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += 1
        
        self.components -= 1


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj = [[] * n for _ in range(n + 1)]
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        dsu = DSU(n)
        for src in range(1, n + 1):
            for dest in adj[src]:
                if dsu.find(src) == dsu.find(dest):
                    return False        
                dsu.union(adj[src][0], dest)
        
        return True
            
        

