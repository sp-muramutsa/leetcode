class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        - capacity
        - one direction
        - trips[]
            - numPassengers, from, to

        - Meeting Rooms II, care about the passengers!!!
        """
        if not trips:
            return False

        trips.sort(key=lambda x: x[1])
        heap = [trips[0]]
        
        if heap[0][0] > capacity:
            return False

        for numPassengers, fro, to in trips[1:]:
            passengers_onboard = numPassengers
            for trip in heap:
                if fro < trip[2]:
                    passengers_onboard += trip[0]

            if passengers_onboard > capacity:
                return False

            heapq.heappush(heap, [numPassengers, fro, to])

        return True

