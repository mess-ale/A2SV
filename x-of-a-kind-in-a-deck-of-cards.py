class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        se = list(dic.values())
        
        mi = min(se)
        l = [1]*(min(se)+1)
        l[0] = l[1] = 0
        for i in range(2, mi+1):
            j = i*i
            while j <= mi:
                l[j] = 0
                j += i
        
        for i,val in enumerate(l):
            if val:
                m = 0
                for j in se:
                    if j % i != 0:
                        break
                    else:
                        m += 1
                if m == len(se):
                    return True
        return False