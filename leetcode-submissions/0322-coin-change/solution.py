class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # BFS: Shortest path

        q = deque([(0, 0)])
        visited = set()

        while q:

            amount_so_far, coins_used = q.popleft()

            if amount_so_far == amount:
                return coins_used

            for coin in coins:

                new_amount_so_far = amount_so_far + coin

                if new_amount_so_far in visited or new_amount_so_far > amount:
                    continue
                
                visited.add(new_amount_so_far)
                q.append((new_amount_so_far, 1 + coins_used))

        return -1

