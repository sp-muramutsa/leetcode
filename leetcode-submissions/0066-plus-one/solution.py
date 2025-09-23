class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Turn the numbers into a string
        # Turn the string into an integer
        # Add one to the integer
        # Turn the digit into a string then back to the int
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        strs = "".join(digits)
        num = int(strs)
        num += 1
        nums = str(num)
        res = []
        for i in nums:
            res.append(int(i))

        return res
