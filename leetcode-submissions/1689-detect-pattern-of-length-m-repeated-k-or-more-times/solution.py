class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # patterns = []
        # for i in range(len(arr)):
        #     patt = ''
        #     count = i
        #     while count < len(arr) and count < i + m:
        #         patt += str(arr[count])
        #         count += 1
        #     patterns.append(patt)
        #     i = count
        # print(patterns)
        # for j in range(len(patterns)):
        #     curr = 1
        #     repeat = True
        #     while curr < k and j + curr < len(patterns):
        #         if patterns[j] != patterns[j + curr]:
        #             break
        #         curr += 1
        #     if curr == k:
        #         return True
        # return False     
        count = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0
            
            if count == (k - 1)*m:
                return True
        return False
