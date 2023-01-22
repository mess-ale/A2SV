class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ls = []
        j = 0
        for i in range(len(s)):
            if j <= len(spaces) - 1:
                if i == spaces[j]:
                    ls.append(" ")
                    j += 1
            ls.append(s[i])

        return "".join(ls)