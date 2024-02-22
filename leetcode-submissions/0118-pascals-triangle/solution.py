class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Time O(numRows ^ 2)
        Space O(numRows)
        """

        pascal_triangle = [[1]]
        for i in range(1, numRows):
            # 1
            list_i = [1] 
            
            # 2
            prev_list = pascal_triangle[i - 1]
            length = len(prev_list)     
            for j in range(length-1):
                list_i.append(prev_list[j] + prev_list[j + 1])
            # 3
            list_i.append(1)
            pascal_triangle.append(list_i)
        return pascal_triangle

        
