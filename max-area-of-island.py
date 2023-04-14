class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        val = 0
        def dfs(r, c):
            nonlocal val
            if grid[r][c] == 0:
                return 
            val += 1
            visited.add((r, c))
            for i in dir:
                new_r = r + i[0]
                new_c = c + i[1]
                if (new_r, new_c) not in visited:
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]):
                        dfs(new_r, new_c)

        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    val = 0
                    dfs(i, j)
                    maxi = max(maxi, val)

        return maxi