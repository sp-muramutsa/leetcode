class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        visited = set(deadends)
        visited.add("0000")
        q = deque([(0, "0000")])

        def get_prev(num: int) -> int:
            return 9 if num == 0 else num - 1

        def get_next(num: int) -> int:
            return 0 if num == 9 else num + 1

        while q:

            turns, curr = q.popleft()

            # Check if it's the goal
            if curr == target:
                return turns

            for i in range(4):
                digit = int(curr[i])
                prev, nxt = get_prev(digit), get_next(digit)

                back_turn = curr[:i] + str(prev) + curr[i + 1 : 4]
                forward_turn = curr[:i] + str(nxt) + curr[i + 1 : 4]

                if back_turn not in visited:
                    visited.add(back_turn)
                    q.append((turns + 1, back_turn))

                if forward_turn not in visited:
                    visited.add(forward_turn)
                    q.append((turns + 1, forward_turn))

        return -1

