class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
            remainders = [score % k for score in arr]
            counter = Counter(remainders)

            for num in remainders:
                partner = (k - num) % k
                print(num, partner)

                if num == partner:
                    if counter[num] % 2 != 0:
                        return False
                else:
                    if num in counter:
                        if partner in counter:
                            if counter[num] != counter[partner]:
                                return False
                        else:
                            return False
                    
            return True
