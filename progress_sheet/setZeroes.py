class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        raw = 0
        lists = []
        while raw < len(matrix):
            test = False
            col = 0
            while col < len(matrix[raw]):
                if matrix[raw][col] == 0:
                    test = True
                    lists.append(col)
                         
                col += 1
            if test:
                matrix[raw] = [0]*len(matrix[raw])
            
            raw += 1
            for i in lists:
                cur_index = 0
                while cur_index < raw:
                    matrix[cur_index][i] = 0
                    cur_index += 1
