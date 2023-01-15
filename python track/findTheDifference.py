class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        ss = sorted(s)
        tt = sorted(t)
        for i in range(0, len(t)):
            if i > len(s)-1:
                return tt[-1]
            if tt[i] == ss[i]:
                continue
            else:
                return tt[i]
