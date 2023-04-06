class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        mult = 1
        def isPrime(x: int) -> bool:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True

        prim = []
        for i in range(2,1000):
            if isPrime(i) == True:
                prim.append(i)
        
        se = set()
        for i in nums:
            j = 0
            while i > 1 and j < len(prim):
                if i%prim[j] == 0:
                    i = i / prim[j]
                    se.add(prim[j])
                else:
                    j += 1

        return len(se)