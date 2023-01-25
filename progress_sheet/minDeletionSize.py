class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col_arranged = []
        if len(strs[0]) == 1:
            col_arranged += [i for i in strs]
        else:
            for i in range(0, len(strs[0])):
                temp = []
                for j in range(0, len(strs)):
                    temp.append(strs[j][i])
                    if len(strs[0]) == 1:
                        temp = []
                if len(strs[0]) > 1:
                    col_arranged.append(temp)
        print(col_arranged)
        count = 0
        if len(strs[0]) == 1:
            s = sorted(col_arranged)
            if col_arranged != s:
                count += 1
        else:
            for i in range(0, len(col_arranged)):
                s = sorted(col_arranged[i])
                if col_arranged[i] != s:
                    count += 1
        return count