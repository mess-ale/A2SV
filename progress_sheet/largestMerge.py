class Solution:
    def largestMerge(self, str1: str, str2: str) -> str:
        
        """
        ans = []
         while len(d1) > 0 and len(d2) > 0:
             if d1[0] > d2[0]:
                 ans.append(d1[0])
                 d1.popleft()
                elif d2[0] > d1[0]:
                    ans.append(d2[0])
                    d2.popleft()
                else:
                    if d1 > d2
        """
        n, m = len(str1), len(str2)
        i = j = 0
        res = ""
        while i < n and j< m:
            if str1[i] > str2[j]:
                res += str1[i]
                i += 1
            elif str1[i] < str2[j]:
                res += str2[j]
                j += 1
            else:
                if str1[i:] > str2[j:]:
                    res += str1[i]
                    i += 1
                else:
                    res += str2[j]
                    j += 1
        return res + str1[i:] + str2[j:]
