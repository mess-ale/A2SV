class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sets = set()
        maxs = 0
        for i in range(0,len(s)):
            while s[i] in sets:
                sets.remove(s[l])
                l += 1
            sets.add(s[i])
            maxs = max(maxs, i-l+1)

        return maxs
