class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # dist = []
        # loc = 0
        # for i in range(len(heights) - 1):
        #     if ladders <= 0:
        #         break
        #     if heights[i] < heights[i + 1]:
        #         dist.append(heights[i + 1] - heights[i])
        #         ladders -= 1
        #         loc = i + 1
        # print(dist, loc)
        # dist.sort()
        # pointer = 0
        # pointer2 = loc
        # for j in range(loc, len(heights) - 1):
        #     pointer2 = j
        #     print(j)
        #     if heights[j] < heights[j + 1]:
        #         diff = heights[j + 1] - heights[j]
        #         if pointer < len(dist) and diff > dist[pointer]:
        #             bricks -= dist[pointer]
        #             pointer += 1
        #         else:
        #             bricks -= diff
        #         if bricks <= 0:
        #             return j
        
        # if pointer2 == len(heights) - 2 and heights[pointer2] >= heights[pointer2 + 1]:
        #     return pointer2 + 1

        # return pointer2

        hq = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(hq, diff)
                if len(hq) > ladders:
                    bricks -= heapq.heappop(hq)
                if bricks < 0:
                    return i
        return len(heights) - 1
            

                
            
        

        

        
