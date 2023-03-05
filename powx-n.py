class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = 1
        if n < 0:
            n = (-n)
            x = 1/x
        while n:
            if n & 1:
                pow *= x

            n = n >> 1

            x = x * x

        return pow