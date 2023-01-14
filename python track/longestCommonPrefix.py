class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        stack = []
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if i > len(strs[j])-1:
                    return "".join(stack)
                elif strs[0][i] == strs[j][i]:
                    
                    continue
                else:
                    return "".join(stack)
                
            stack.append(strs[0][i])
            
        return "".join(stack)
                    
                    
