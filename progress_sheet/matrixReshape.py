class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        lists = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lists.append(mat[i][j])

        if len(lists) != r*c:
            return mat   

        result = []
        for i in range(r):
            result.append([])
        
        s = c
        for i in range(r):
            for j in range(s-c,s):
                result[i].append(lists[j])
                s += 1

        return result
