class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = [str(i) for i in nums]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if int(s[i][0]) <= int(s[j][0]):
                    if int(s[i][0]) == int(s[j][0]):
                        forward = []
                        backward = []
                        forward.append(s[i][1:])
                        forward.append(s[j])
                        backward.append(s[j][1:])
                        backward.append(s[i])
                        if int("".join(forward)) < int("".join(backward)):
                            s[i], s[j] = s[j], s[i]
                    else:
                        s[i], s[j] = s[j], s[i]
        return str(int("".join(s)))
