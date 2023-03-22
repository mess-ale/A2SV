class Solution(object):
    def shortestSubarray(self, A, K):
        prefix = [0] 
        for i in A: prefix.append(prefix[-1] + i) 
        ans = float('inf')
        deque = collections.deque([0])
        for i in range(1, len(A)+1):
            while deque and prefix[i] - prefix[deque[0]] >= K:
                ans = min(ans, i - deque.popleft()) 
            while deque and prefix[deque[-1]] >= prefix[i]:
                deque.pop() 
            deque.append(i) 
        return ans if ans != float('inf') else -1