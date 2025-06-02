class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = {}
        def tot(num):
            res = []
            tot = 0
            word = str(num)
            for i in word:
                res.append(int(i))
            for j in res:
                tot += j ** 2
            return tot
        value = n
        while True:
            val = tot(value)
            if value in hashmap:
                return False
            elif value == 1:
                return True
            else:
                hashmap[value] = val
            value = val
