class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s):
            return s.count(min(s))
        
        fq = [f(q) for q in queries]
        fw = sorted([f(w) for w in words])
        
        return [len(fw) - bisect_right(fw, q) for q in fq]