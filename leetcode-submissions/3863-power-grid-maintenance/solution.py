class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(1, n + 1)}
        self.sizes = {i: 0 for i in range(1, n + 1)}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return x

        size_x = self.sizes[parent_x]
        size_y = self.sizes[parent_y]

        if size_x > size_y:
            self.parents[parent_y] = parent_x
            self.sizes[parent_x] += self.sizes[parent_y]
        else:
            self.parents[parent_x] = parent_y
            self.sizes[parent_y] += self.sizes[parent_x]


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:

        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        for k in dsu.parents:
            dsu.parents[k] = dsu.find(k)

        online = {i: True for i in range(1, c + 1)}
        component_heaps = defaultdict(list)
        result = []

        for k, v in dsu.parents.items():
            heapq.heappush(component_heaps[v], k)

        for request, x in queries:
            if request == 1:
                ans = None
                if online[x]:
                    ans = x
                else:
                    root = dsu.find(x)
                    while component_heaps[root]:
                        smallest = heapq.heappop(component_heaps[root])
                        if online[smallest]:
                            ans = smallest
                            heapq.heappush(component_heaps[root], smallest)
                            break
                    if not ans:
                        ans = -1

                result.append(ans)

            elif request == 2:
                online[x] = False

        return result

