class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        ls = []
        for i in range(n):
            ls.append(i+1)
        i = k - 1
        while len(ls) > 1:
            if i > len(ls)-1:
                i = i % len(ls)
            del ls[i]
            i += k-1
        return ls[0]
