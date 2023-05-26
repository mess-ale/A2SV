class Solution:
    def climbStairs(self, n: int) -> int:
        memory = [0]*n
        def depy(x):
            if x == 0 or x == 1:
                return 1
            if x-1 in memory:
                return memory[x-1]
            memory[x-1] = depy(x-1)+depy(x-2)
            return memory[x-1]
        return depy(n)