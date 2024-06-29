class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            while i < len(line):
                if not in_block and line[i:i+2] == '/*':
                    in_block = True
                    i += 1
                elif in_block and line[i:i+2] == '*/':
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            if new_line and not in_block:
                ans.append("".join(new_line))
        return ans    
        
        # to_remove = []
        # for i in range(len(source)):
        #     if '//' in source[i]:
        #         source[i] = source[i][0:source[i].find('//')]
        #     elif '/*' in source[i]:
        #         k = i
        #         while('*/' not in source[k]):
        #             to_remove.append(source[k])
        #             k += 1
        #         to_remove.append(source[k])
        #         i = k
        # for elem in to_remove:
        #     if elem in source:
        #         source.remove(elem)
        # return source
        
