class Solution:   
    def scoreOfParentheses(self, s: str) -> int:
        stck = []
        for ch in s:
            if ch == ')':
                cur = 0
                while stck[-1] > 0:
                    cur += stck.pop()
                stck.pop()
                stck.append(max(2*cur, 1))
            else:
                stck.append(0)
        return sum(stck)