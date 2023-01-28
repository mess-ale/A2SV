class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        i = 0
        limit = floor(sqrt(c))
        while i <= limit:
            if i*i + limit*limit == c:
                return True
            elif i*i + limit*limit > c:
                limit -= 1
            else:
                i += 1

        return False
