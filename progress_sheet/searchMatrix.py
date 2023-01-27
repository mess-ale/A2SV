class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i <= j:
            if matrix[i][-1] >= target:
                if target in matrix[i]:
                    return True
            if matrix[j][0] <= target:
                if target in matrix[j]:
                    return True
            i += 1
            j -= 1
        return False