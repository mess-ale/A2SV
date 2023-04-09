class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def prime_sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False
            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                while j <= n:
                    is_prime[j] = False
                    j += i
                i += 1
            return is_prime

        prime = prime_sieve(right)
        ans = []
        for i in range(left, right+1):
            if prime[i] == True:
                ans.append(i)
            
        res = []
        i = 0
        j = 1
        mini = float("inf")
        while j < len(ans):
            if mini > min(mini, ans[j]-ans[i]):
                res = [ans[i], ans[j]]
                mini = min(mini, ans[j]-ans[i])
            i += 1
            j += 1
        if len(res) != 2:
            return [-1,-1]
            
        return res