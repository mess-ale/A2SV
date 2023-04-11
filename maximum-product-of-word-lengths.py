class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        ans = 0
        for j in range(len(words)):
            bit_masking = [0]*26
            for i in set(words[j]):
                if bit_masking[ord(i)%97] == 0:
                    bit_masking[ord(i)%97] = 1
            
            for i in range(j+1, len(words)):
                flage = True
                for m in set(words[i]):
                    if bit_masking[ord(m)%97] == 1:
                        flage = False
                        break
                if flage:
                    ans = max(ans, len(words[j]) * len(words[i]))

        return ans