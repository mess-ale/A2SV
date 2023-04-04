class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def helper(arr):
            count = 0
            x = 0
            while x + 2 < len(arr[0]):
                arry = set()
                di = set()
                for i in range(3):
                    raw = 0
                    col = 0
                    for j in range(x, x+3):
                        raw += arr[j-x][i+x]
                        col += arr[i][j]
                        if 0 < arr[i][j] <= 9:
                            di.add(arr[i][j])
                            
                    arry.add(raw)
                    arry.add(col)
                dig1 = 0
                dig2 = 0
                for i in range(x, x+3):
                    dig1 += arr[i-x][i]
                    dig2 += arr[i-x][2*(x+1)-i]
                    
                arry.add(dig1)
                arry.add(dig2)
                
                if len(arry) == 1 and len(di) == 9:
                    count += 1
                x += 1

            return count

        i = 0
        ans = 0
        while i+2 < len(grid):
            ans += helper(grid[i:i+3])
            i += 1

        return ans