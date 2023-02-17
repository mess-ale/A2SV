class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy = []
        for i in range(0, len(matrix)):
            temp = []
            for j in range(0, len(matrix)):
                temp.append(matrix[i][j])
            copy.append(temp)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                matrix[i][j] = copy[len(matrix)-j-1][i]
