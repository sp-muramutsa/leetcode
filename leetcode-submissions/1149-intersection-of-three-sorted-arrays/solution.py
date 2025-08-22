class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # We make all of them sets
        # We iterate through one set and chak if they are in others and add them to the result
        result = []
        s1 = set()
        for i in arr1:
            s1.add(i)
            
        s2 = set()
        for j in arr2:
            s2.add(j)
            
        s3 = set()
        for z in arr3:
            s3.add(z)
            
        for k in s1:
            if k in s2 and k in s3:
                result.append(k)
                
        return sorted(result)
