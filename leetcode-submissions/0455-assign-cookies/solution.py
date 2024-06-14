class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Time: O(nlogn)
        Intuition: Use two pointers. Move the one in the cookies freely to find cookies that can satisfy children. Only move the one in children when you find a cookie that can satisfy them. Make sure the biggest cookies and the greediest children are considered first.
        """

        length_g, length_s = len(g), len(s)
        s = sorted(s, reverse=True)
        g = sorted(g, reverse=True)

        i, j  = 0, 0
        result = 0

        while i < length_g and j < length_s:
            if s[j] >= g[i]:
                result += 1
                j += 1
            i += 1
        
        return result

        
