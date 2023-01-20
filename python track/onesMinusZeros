class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        col_ones = []
        raw_ones = []
        col_length = len(grid[0])
        raw_length = len(grid)
        for i in range(0, len(grid)):
            temp1 = 0
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    temp1 += 1
            raw_ones.append(temp1)

        for i in range(0, len(grid[0])):
            temp1 = 0
            for j in range(0, len(grid)):
                if grid[j][i] == 1:
                    temp1 += 1
            col_ones.append(temp1)
        print(raw_ones)
        print(col_ones)
        ans = []
        for i in range(0, raw_length):
            temp = []
            for j in range(0, col_length):
                temp.append(raw_ones[i]+col_ones[j] - (raw_length-raw_ones[i]) - (col_length-col_ones[j]))
            ans.append(temp)
        return ans
