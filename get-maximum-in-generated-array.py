class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
            
        if n < 3:
            return 1

        arr = [0]*(n+1)
        arr[1] = 1
        
        def melt(nn):
            if nn == 0:
                return 0
            if nn == 1:
                return 1
            
            if (nn-1)*2 <= n:
                arr[(nn-1)*2] = melt(nn-1)
            if (nn-1)*2+1 <= n:    
                arr[(nn-1)*2+1] = arr[(nn-1)]+arr[(nn-1)+1]
            return arr[(nn-1)+1]
            
        melt(n//2+1)
        return max(arr)