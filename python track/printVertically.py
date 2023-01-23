class Solution:
    def printVertically(self, s: str) -> List[str]:

        s_split = s.split()
        max_num = 0
        ans = []
        for i in range(len(s_split)):
            s_split[i] = [i for i in s_split[i]]
            max_num = max(max_num, len(s_split[i]))

        for i in range(max_num):
            temp = []
            for j in range(len(s_split)):
                if i >= len(s_split[j]):
                    temp.append(" ")
                else:
                    temp.append(s_split[j][i])

            ans.append("".join(temp).rstrip())

        return ans