from random import randint

class Solution:
    # def quicksort(self, arr: List[List[int]]) -> List[List[int]]:
    #     if len(arr) < 2:
    #         return arr
        
    #     low, same, high = List[], List[], List[]
    #     pivot = arr[randint(0, len(arr) -1)][1]

    #     for item in arr:
    #         if item[1] < pivot:
    #             low.append(item)
    #         elif item[i] > pivot:
    #             high.append(item)
    #         else:
    #             same.append(item)
        
    #     return quicksort(low) + same + quicksort(high)


    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        '''
        score each cities edges... sort... assign based off of that...
        then find the answer
        '''

        edges = [0] * n
        for i in range(len(roads)):
            edges[roads[i][0]] += 1
            edges[roads[i][1]] += 1
        
        edges.sort()

        # currRoad = List[List[int]]
        # for j in range(len(edges)):
        #     currRoad.add([j, edges[j]])
        
        # currRoad = quicksort[roads]
        # ans = 0
        # for edge in roads:
        value = 1
        maximum = 0
        for edge in edges:
            maximum += value * edge
            value += 1
        return maximum


        #the rank is the location on the sorted array
        #go through the edges and sum up the ranks







