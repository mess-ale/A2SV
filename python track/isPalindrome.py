class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        else:
            xx = [int(i) for i in str(x)]
            xxx = []
            for i in range(len(xx)-1,-1,-1):
                xxx.append(xx[i])
            if xx == xxx:
                return True
            else:
                return False
