class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        answer = []
        min_number = min(len(word1), len(word2)) 
        for i in range(0, min_number):
            answer.append(word1[i])
            answer.append(word2[i])
        if len(word1) > len(word2):
            answer.append(word1[min_number:])
        else:
            answer.append(word2[min_number:])
        return "".join(answer)
            
