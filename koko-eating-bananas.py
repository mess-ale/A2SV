class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            hours = 0
            mid = left + (right-left)//2
            for i in piles:
                hours += ceil(i/mid)

            if h < hours:
                left = mid + 1
            else:
                right = mid

        return right
        
        
        
        
        
        
        
        
        
        
        
        
        
        # piles.sort()

        # left = 0
        # right = len(piles)
        # while left < right:
        #     mid = left + (right-left)//2