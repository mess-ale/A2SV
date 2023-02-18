class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        start_col,end_col,start_raw,end_raw = 0,len(matrix[0]),0,len(matrix)
        while start_col<end_col or start_raw<end_raw:
            if start_raw<end_raw:
                for i in range(start_col, end_col):
                    result.append(matrix[start_raw][i])
            start_raw += 1

            if start_col<end_col:
                for i in range(start_raw, end_raw):
                    result.append(matrix[i][end_col-1])
            end_col -= 1

            if start_raw<end_raw:
                for i in range(end_col-1, start_col-1,-1):
                    result.append(matrix[end_raw-1][i])
            end_raw -= 1

            if start_col<end_col:
                for i in range(end_raw-1, start_raw-1,-1):
                    result.append(matrix[i][start_col])
            start_col += 1
        print(result)
        return result
