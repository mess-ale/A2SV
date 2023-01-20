class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        ls = []
        for i in words:
            ls.append(set(i))

        result = []
        for i in range(0, len(ls)):
            for j in range(i+1, len(ls)):
                if ls[i] == ls[j]:
                    temp = []
                    temp.append(ls[i])
                    temp.append(ls[j])
                    result.append(temp)
                    
        return len(result)

