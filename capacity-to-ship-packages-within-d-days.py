class Solution:
    def shipWithinDays(self, weights, D):
        def helper(target, D):
            cnt = 0
            cur = 0 
            for w in weights:
                if cur+w>mid:
                    cnt+=1
                    cur=0
                cur+=w
            return cnt>=D

        left = max(weights)
        right = sum(weights)
        
        while left<=right:
            mid = (left+right)//2
            if helper(mid, D):
                left = mid+1
            else:
                right = mid-1
            
        return left