class Solution:
    def findComplement(self, num: int) -> int:
        ls = []
        while num >= 1:
            num = num / 2
            if num%1 != 0:
                ls.append(1)
                num = floor(num)

            else:
                ls.append(0)


        for i in range(len(ls)):
            if ls[i] == 1:
                ls[i] = 0
            else:
                ls[i] = 1

        sums = 0
        for i in range(len(ls)):
            sums += (2**(i))*ls[i]
        return sums