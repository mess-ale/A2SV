class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winner = defaultdict(int)
        losser = defaultdict(int)
        result = [[],[]]
        for i in range(len(matches)):
            winner[matches[i][0]] = winner[matches[i][0]] + 1
            losser[matches[i][1]] = losser[matches[i][1]] + 1
        
        for key,value in winner.items():
            if losser.get(key) is None: 
                result[0].append(key)
        for key in losser:
            if losser[key] > 1:
                continue
            else:
                result[1].append(key)
        result[0].sort()
        result[1].sort()
        return result
