class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def create(row, step):
            if step == rowIndex:
                return row



            level = [1]
            if len(row) >= 2:
                for j in range(1,len(row)):
                    level.append(row[j-1] + row[j])

            level.append(1)
            return create(level, step + 1)
        return create([1], 0)
        
        # arr = [[1]]
        # for i in range(rowIndex):
        #     level = [1]
        #     if len(arr[-1]) >= 2:
        #         for j in range(1,len(arr[-1])):
        #             level.append(arr[-1][j-1] + arr[-1][j])

        #     level.append(1)
        #     arr.append(level)