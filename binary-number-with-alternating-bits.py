class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)
        ls = []
        for i in n[::-1]:
            if i == "b":
                break
            ls.append(i)

        for i in range(1, len(ls)):
            if ls[i] != ls[i-1]:
                continue
            else:
                return False

        return True