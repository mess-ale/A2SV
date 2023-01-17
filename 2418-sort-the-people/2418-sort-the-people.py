class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
                    
        return names