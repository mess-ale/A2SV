class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            lar1 = heappop(stones)
            lar2 = heappop(stones)
            if lar1 == lar2:
                continue
            else:
                if lar1 < lar2:
                    heappush(stones, lar1-lar2)
                else:
                    heappush(stones, lar2-lar1)
        
        if stones:
            return stones[0]*(-1)
        return 0