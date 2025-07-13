import heapq
from collections import Counter
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        max_heap = [-x for x in counter.values()]
        heapq.heapify(max_heap)

        pq = deque([])
        time = 0

        while max_heap or pq:
            time += 1

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1

                if freq < 0:
                    pq.append((freq, time + n))

            if pq and pq[0][1] == time:
                new_freq, _ = pq.popleft()
                heapq.heappush(max_heap, new_freq)

        return time

