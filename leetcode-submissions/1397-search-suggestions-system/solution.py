class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        n = len(searchWord)
        m = len(products)
        suggestions = []

        for i in range(n):
            prefix = searchWord[: i + 1]
            top_3 = []

            l, r = 0, m

            while l < r:
                mid = l + (r - l) // 2
                if products[mid] < prefix:
                    l = mid + 1
                else:
                    r = mid

            end = min(l + 3, m)
            for i in range(l, end):
                if products[i].startswith(prefix):
                    top_3.append(products[i])

            suggestions.append(top_3)

        return suggestions

