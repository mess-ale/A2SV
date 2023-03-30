class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x >= 1:
            x = x/2
            if x%1 != 0:
                y += 1
                x = floor(x)

            
        return y