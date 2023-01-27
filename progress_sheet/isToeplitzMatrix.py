class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = 0
        j = 0
        count = 1
        while count < len(matrix[0]):
            if len(matrix[0])>j+1 and len(matrix)>i+1:
                if matrix[i][j] !=matrix[i+1][j+1]:
                    return False
                else:
                    i += 1
                    j += 1
            else:
                i = 0
                j = count
                count += 1
        i = 1
        j = 0
        count = 1
        while count < len(matrix)-1:
            if len(matrix[0])>j+1 and len(matrix)>i+1:
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                else:
                    i += 1
                    j += 1
            else:
                count += 1
                i = count
                j = 0
        return True