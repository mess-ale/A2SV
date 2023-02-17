class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        raw = 0
        col = 0
        while True:
            lists = []
            for i in range(raw, raw+3):
                for j in range(col, col+3):
                    if board[i][j] != ".":
                        lists.append(board[i][j])
            lists.sort()
            for i in range(0,len(lists)-1):
                if lists[i] == lists[i+1]:
                    return False
            
            if col+3 > 8:
                if col+3 > 8 and raw +3 >8:
                    break
                raw += 3
                col = 0
            else:
                col += 3
                
        raw_list = []
        col_list = []
        for i in range(0, 9):
            temp1 = []
            temp2 = []
            for j in range(0, 9):
                if board[i][j] != '.':
                    temp1.append(board[i][j])
                if board[j][i] != '.':
                    temp2.append(board[j][i])
            raw_list.append(temp1)
            col_list.append(temp2)
            
            
        for i in range(0,len(raw_list)):
            for j in range(0, len(raw_list[i])-1):
                m = sorted(raw_list[i])
                if m[j] == m[j+1]:
                    return False
                    
                     
        for i in range(0,len(col_list)):
            for j in range(0, len(col_list[i])-1):
                s = sorted(col_list[i])
                if s[j] == s[j+1]:
                    return False
                
        return True
