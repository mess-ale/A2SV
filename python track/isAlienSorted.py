class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        lookup = {c:ix for ix,c in enumerate(order)}
        
        words2 = []
        for w in words:
            tmp = []
            for c in w:
                tmp.append(lookup[c])
            words2.append(tmp)
            
        for i in range(1, len(words2)):
            if words2[i-1]>words2[i]:
                return False
        return True
