class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_val = 0
        left = 0
        dec = {}

        for i in range(len(s)):
            dec[s[i]] = dec.get(s[i], 0) + 1

            while i-left+1-max(dec.values()) > k:
                dec[s[left]] -= 1
                left += 1

            max_val = max(max_val, i-left+1)
            print(dec)
        return max_val
