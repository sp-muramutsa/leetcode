class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        result = set()


        a = 0
        while a < n:           
            # 3sum          
            b = a + 1
            while b < n:
                c, d = b + 1, n - 1
                while c < d:
                    foursome = nums[a] + nums[b] + nums[c] + nums[d]
                    # equal
                    if foursome == target:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1                     
                    
                    # left
                    elif foursome < target:
                        c += 1

                    # right 
                    else:
                        d -= 1
                b += 1
            a += 1
  

        return result 

                    
                  



                


         
