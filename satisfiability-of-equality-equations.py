class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))
        rank = [0]*26

        def find(x):
            if parent[x] == x:
                return x

            ans = find(parent[x])
            parent[x] = ans
            return ans
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return
            if rank[rootx] > rank[rooty]:
                rootx, rooty = rooty, rootx
            parent[rootx] = rooty
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1

        for i,j,k,l in equations:
            if j == "=":
                union(ord(i)%97,ord(l)%97)
        for i,j,k,l in equations:
            if j == "!":
                if find(ord(i)%97) == find(ord(l)%97):
                    return False

        return True