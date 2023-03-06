class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefixsum1 = [0]
        prefixsum2 = [0]
        cur = 0
        for i in grid[0]:
            cur += i
            prefixsum1.append(cur)

        cur = 0
        for i in grid[1]:
            cur += i
            prefixsum2.append(cur)
        
        minval = float("inf")
        for i in range(1, len(prefixsum1)):
            newval1 = prefixsum1[len(prefixsum1)-1] - prefixsum1[i]
            newval2 = prefixsum2[i-1]
            minval = min(minval, max(newval1,newval2))
            
        return minval