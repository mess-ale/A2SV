class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        raw = 0
        col = 0
        result = []
        temp = []
        while True:
            maxs = float("-inf")
            for i in range(raw, raw+3):
                for j in range(col, col+3):
                    if max(maxs, grid[i][j]) > maxs:
                        maxs = max(maxs, grid[i][j])

            temp.append(maxs)
            if col+3 > len(grid[0])-1:
                result.append(temp)
                temp = []
                raw += 1
                col = 0
            else:
                col += 1
            
            if raw+3 > len(grid):
                break
           
        return result
