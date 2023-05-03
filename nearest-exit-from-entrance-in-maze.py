class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        qe = deque()
        qe.append(entrance)
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        visited.add((entrance[0], entrance[1]))
        s = -1
        flage = True

        while qe and flage:
            le = len(qe)

            for j in range(le):
                for i in dir:
                    r = i[0] + qe[0][0]
                    c = i[1] + qe[0][1]

                    if -1<r<len(maze) and -1<c<len(maze[0]):
                        if (r,c) not in visited:
                            if maze[r][c] == ".":
                                qe.append([r,c])
                                visited.add((r,c))
                                
                    else:
                        if [qe[0][0], qe[0][1]] != entrance:
                            flage = False
                
                qe.popleft()
            s += 1

        if not flage:
            return s
        return -1