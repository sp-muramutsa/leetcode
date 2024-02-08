class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()   
        count = len(nums)
        for i in range(count):
            a = i + 1
            b = count - 1

            while a < b:
                if nums[a] + nums[i] + nums[b] == 0:
                    triplets.add((nums[a], nums[i], nums[b]))
                    a += 1
                    b -= 1

                elif nums[a] + nums[i] + nums[b] < 0:
                    a += 1
                
                else:
                    b -= 1
        
        return triplets
            
        
        
        

        
