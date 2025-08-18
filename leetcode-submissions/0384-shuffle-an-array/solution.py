class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.arr = nums

    def reset(self) -> List[int]:
        self.arr = self.original.copy()
        return self.arr

    def shuffle(self) -> List[int]:
        n = len(self.original)
        for i in range(n):
            j = random.randrange(n)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

