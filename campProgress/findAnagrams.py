class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        wind = Counter(s[0:len(p)])
        sec = Counter(p)
        for i in range(0, len(s)-len(p)+1):
            if wind == sec:
                result.append(i)
            if wind[s[i]] <= 1:
                del wind[s[i]]
            else:
                wind[s[i]] -= 1
            if i+len(p) > len(s)-1:
                if wind == sec:
                    result.append(i)
            else:
                wind[s[i+len(p)]] = wind.get(s[i+len(p)],0) + 1
            
        return result
