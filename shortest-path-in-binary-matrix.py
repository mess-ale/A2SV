class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid)==1 and grid[0][0]==0:
            return 1

        if grid[0][0]!=0 or grid[len(grid)-1][len(grid)-1]!=0:
            return -1

        qe = deque()
        qe.append([0,0])
        visited = set()
        visited.add((0, 0))
        dir = [[0,1], [0,-1], [1,0], [-1,0], [-1,1], [-1,-1], [1,-1], [1,1]]
        pos = 1
        while qe:
            pos += 1
            le = len(qe)
            
            for j in range(le):
                for i in dir:
                    r = qe[0][0] + i[0]
                    c = qe[0][1] + i[1]

                    if -1<r<len(grid) and -1<c<len(grid):
                        if grid[r][c] == 0:
                            if r==len(grid)-1 and c==len(grid)-1 and grid[r][c]==0:
                                return pos
                            if (r, c) not in visited:
                                qe.append([r, c])
                                visited.add((r, c))
                qe.popleft()
            
        return -1