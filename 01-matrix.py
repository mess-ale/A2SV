class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        qe = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    qe.append((i,j))
                    visited.add((i, j))

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        s = 0
        while qe:
            s += 1
            le = len(qe)
            
            for i in range(le):
                for j in dir:
                    r = qe[0][0]+j[0]
                    c = qe[0][1]+j[1]

                    if -1<r<len(mat) and -1<c<len(mat[0]):
                        if mat[r][c] == 1:
                            if (r, c) not in visited:
                                visited.add((r, c))
                                mat[r][c] = s
                                qe.append((r, c))
                qe.popleft()

        return mat






        




        # self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # visited = set()
        # self.path = []
        # def bfs(se):
        #     s = 0
        #     while se:
        #         s += 1
        #         le = len(se)
        #         temp = []
        #         for i in range(le):
        #             temp.append(se[0])
        #             for j in self.dir:
        #                 r = se[0][0]+j[0]
        #                 c = se[0][1]+j[1]
        #                 if -1<r<len(mat) and -1<c<len(mat[0]):
        #                     if mat[r][c] == 0:
        #                         return
        #                     se.append([r, c])
        #             se.popleft()
        #         self.path.append(temp)

        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 1:
        #             for k,val in enumerate(self.path):
        #                 if [i, j] in val:
        #                     mat[i][j] = k
        #                     continue
        #             se = deque()
        #             se.append([i, j])
        #             mat[i][j] = bfs(se)
        
        # return mat