class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        dec = defaultdict(list)
        ans = 0
        for i in range(len(isConnected)):
            for j,val in enumerate(isConnected[i]):
                if j != i and val == 1:
                    dec[j+1].append(i+1)
        visited = set()
        def dfs(dec, val):
            visited.add(val)
            for i in dec[val]:
                if i not in visited:
                    dfs(dec, i)
                    dec[i] = []
        print(dec)
        for i in dec:
            if i not in visited:
                dfs(dec, i)
        print(dec)
        for i in dec:
            if dec[i]:
                ans += 1
        return ans+(len(isConnected) - len(dec))