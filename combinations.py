class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinetion = []
        def combiner(ns, path):
            if len(path) == k:
                combinetion.append(path[:])
                return 

            for i in range(ns, n+1):
                path.append(i)
                combiner(i+1, path)
                path.pop()

            
        combiner(1, [])
        return combinetion