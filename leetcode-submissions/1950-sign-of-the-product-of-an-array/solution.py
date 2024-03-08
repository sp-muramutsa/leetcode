class Solution:
    def arraySign(self, nums: List[int]) -> int:
       
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1   
            return 0
        
        product = 1    
        for number in nums:
            product *= number
        
        return signFunc(product)




             
        
