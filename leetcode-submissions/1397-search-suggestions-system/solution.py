class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # cut the searchWord into prefixes
        prefixes = []
        word_length = len(searchWord)
        i = 1
        while i < word_length + 1:
            prefixes.append(searchWord[:i])
            i += 1
        
        
        # for each prefix: create a list of related words
        search_suggestion = []
        for prefix in prefixes:
            prefix_length = len(prefix)
            prefix_product = []
            for product in products:
                if product[:prefix_length] == prefix:
                    prefix_product.append(product)

            # sort lexicographically
            prefix_product = sorted(prefix_product)

            # return at most the top three words
            try:
                search_suggestion.append(prefix_product[:3])
            except IndexError:
                search_suggestion.append(prefix_product)
            
        return search_suggestion



        
        
            
                    


    
        
