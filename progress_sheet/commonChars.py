
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        count = []
        first_word_count = Counter(words[0]) 
        ans = [0]*26

        for key,value in  first_word_count.items():
            ans[ord(key) % ord('a')] = value

        for i in range(len(words)):
            count = Counter(words[i])
            for j in range(len(ans)):
                letter = chr(j + ord('a'))
                ans[j] = min(ans[j], count[letter])

        result = []
        for i in range(len(ans)):
            result += [chr(i + ord('a'))]*ans[i]
            
        return result
            
