class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def recreation(row):
            if row < 2:
                return [1]*(row+1)
            curr = recreation(row-1)
            
            val = [1]
            for i in range(1,row):
                val.append(curr[i-1]+curr[i])
            val.append(1)
            return val

        return recreation(rowIndex)