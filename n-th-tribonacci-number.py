class Solution:
    def tribonacci(self, n: int) -> int:
        
        memory = [0]*n
        def hepy(x):
            if x == 0:
                return 0
            if x == 1 or x == 2:
                return 1
            if memory[x-1] != 0:
                return memory[x-1]
            memory[x-1] = hepy(x-1)+hepy(x-2)+hepy(x-3)
            return memory[x-1]

        return hepy(n)