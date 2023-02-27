class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        wind = Counter(t)
        dec = defaultdict(int)
        sub_array = [0, len(s)]
        left = 0
        count = 0
        for right in range(len(s)):
            if s[right] in wind:
                dec[s[right]] += 1
                if dec[s[right]] == wind[s[right]]:
                    count += 1
                
            while left <= right and count == len(wind):
                if sub_array[1]-sub_array[0]+1 > right - left + 1:
                    sub_array[0] = left
                    sub_array[1] = right
                if s[left] in wind:
                    dec[s[left]] -= 1
                    if dec[s[left]] < wind[s[left]]:
                        count -= 1
                left += 1
        
        if sub_array[1]-sub_array[0]+1 > len(s):
            return ""

        return s[sub_array[0]:sub_array[1]+1]
