class Solution:
    # def isPossible(self, n: int, edges: List[List[int]]) -> bool:
    #     degree = [0]*n
    #     for edge in edges:
    #         degree[edge[0] - 1] += 1
    #         degree[edge[1] - 1] += 1
        
    #     odds = []
    #     for k in range(len(degree)):
    #         if degree[k] % 2 == 1:
    #             odds.append(k + 1) 
    #     if len(odds) == 0: 
    #         return True
    #     if len(odds) == 1 or len(odds) == 3 or len(odds) > 4:
    #         return False
    #     #two odd and there is an even neither of them connect to, can use that two add two edges
    #     if len(odds) == 2:
    #         if [odds[0], odds[1]] not in edges and [odds[1], odds[0]] not in edges:
    #             return True
    #         for curr in range(1,n+1):
    #             if curr != odds[0] and curr != odds[1] and [curr, odds[0]] not in edges and [odds[0], curr] not in edges and [curr, odds[1]] not in edges and [odds[1], curr] not in edges:
    #                 return True
    #         return False 
                     
    #     if (len(odds) == 4 and 
    #         (
    #             ([odds[0], odds[1]] not in edges and [odds[1], odds[0]] not in edges and 
    #             [odds[2], odds[3]] not in edges and [odds[3], odds[2]] not in edges) or 
    #             ([odds[1], odds[2]] not in edges and [odds[2], odds[1]] not in edges and 
    #             [odds[0], odds[3]] not in edges and [odds[3], odds[0]] not in edges) or
    #             ([odds[1], odds[3]] not in edges and [odds[3], odds[1]] not in edges and 
    #             [odds[2], odds[0]] not in edges and [odds[0], odds[2]] not in edges)
    #         )):
    #         return True 
    #     return False 


    '''
    need to use a graph that maps a node to its neighbors, so it's easy to check if they are neigbors... instead of parsing through edges everytime
    '''

    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for i in range(n)]
        for edge in edges:
            graph[edge[0] - 1].add(edge[1] - 1)
            graph[edge[1] - 1].add(edge[0] - 1)
        
        odds = []
        for k in range(n):
            if len(graph[k]) % 2 == 1:
                odds.append(k)
        if len(odds) == 0: 
            return True
        if len(odds) == 1 or len(odds) == 3 or len(odds) > 4:
            return False
        if len(odds) == 2:
            a, b = odds
            if [a + 1, b + 1] not in edges and [b + 1, a + 1] not in edges:
                return True
            for curr in range(n):
                if curr not in graph[a] and curr not in graph[b]:
                    return True
            return False 
                        
        if len(odds) == 4:
            a, b, c, d = odds
            if ((a not in graph[b] and c not in graph[d]) or (a not in graph[c] and b not in graph[d]) or (a not in graph[d] and b not in graph[c])):
                return True
        return False
