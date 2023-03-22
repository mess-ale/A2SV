class Solution(object):
    def sumSubarrayMins(self, A):
        mod = 10 ** 9 + 7
        left = self.f(A)
        right = self.g(A)
        cs = 0
        for i in range(len(A)): cs = (cs + left[i] * right[i] * A[i]) % mod
        return cs
        
    def f(self,A):
        stack = collections.deque([])
        left = [0] * len(A)
        for i in range(len(A)):
            while(stack and A[stack[-1]] > A[i]): stack.pop()
            left[i] = i - (stack[-1] if stack else -1)
            stack.append(i)
        return left
    def g(self,A):
        stack = collections.deque([])
        right = [0] * len(A)
        for i in range(len(A)-1,-1,-1):
            while(stack and A[stack[-1]] >= A[i]): stack.pop()
            right[i] = (stack[-1] if stack else len(A)) - i
            stack.append(i)
        return right