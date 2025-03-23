class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_product = []
        current_product = 1
        for i in range(len(nums)):
            if i == 0:
                prefix_product.append(1)
            else:
                current_product = current_product * nums[i-1]
                prefix_product.append(current_product)
        print(prefix_product )


        suffix_product = []
        current_product_1 = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix_product.append(1)
            else:
                current_product_1 = current_product_1 * nums[i+1]
                suffix_product.append(current_product_1)
        suffix_product = suffix_product[-1::-1]
        print(suffix_product)

        for i in range(len(prefix_product)):
            res.append(prefix_product[i]*suffix_product[i])
        return res
        
        

         
