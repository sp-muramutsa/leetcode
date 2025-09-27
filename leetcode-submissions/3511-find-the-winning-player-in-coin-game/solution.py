class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        n = min(x, y//4)
        return "Bob" if n % 2 == 0 else "Alice"
