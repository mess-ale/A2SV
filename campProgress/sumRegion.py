class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.horizontalprifex = []
        for i in range(len(matrix)):
            temp = []
            cur = 0
            for j in range(len(matrix[0])):
                cur += matrix[i][j]
                temp.append(cur)
            self.horizontalprifex.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        startcol = 1
        if col1 == 0:
            startcol = 0
            
        for i in range(row1, row2+1):
            sums += self.horizontalprifex[i][col2]-self.horizontalprifex[i][col1-1]*startcol
        return sums






# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
