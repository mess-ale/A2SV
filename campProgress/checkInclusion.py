class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wind = Counter(s2[:len(s1)])
        val = Counter(s1)
        if val == wind:
            return True 
        for i in range(0, len(s2)-len(s1)):
            if val == wind:
                return True
            wind[s2[i]] -= 1
            if wind[s2[i]] == 0:
                del wind[s2[i]]
            wind[s2[i+len(s1)]] = wind.get(s2[i+len(s1)],0)+1
            if val == wind:
                return True
        return False
