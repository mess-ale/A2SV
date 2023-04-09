class Solution:
    def minSteps(self, n: int) -> int:
        def isprime(n):
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        prime = []
        for i in range(2, n+1):
            if isprime(i):
                prime.append(i)

        if not prime:
            return n

        ans = []
        i = 0
        while n > 1 and i < len(prime):
            if n % prime[i] == 0:
                n = n / prime[i]
                ans.append(prime[i])
            else:
                i += 1

        return sum(ans)