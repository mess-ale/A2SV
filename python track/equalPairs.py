class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        raw_list = []
        col_list = []
        for i in range(len(grid)):
            temp1 = []
            temp2 = []
            for j in range(len(grid[0])):
                temp1.append(grid[i][j])
                temp2.append(grid[j][i])
            raw_list.append(temp1)
            col_list.append(temp2)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if raw_list[i] == col_list[j]:
                    counter += 1

        return counter