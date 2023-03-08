class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 and k == 1:
            return "0"

        def reverse(arr):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
            return arr[::-1]
            
        lis = []
        def findKth(n):
            nonlocal lis
            if n == 2:
                lis.append(0)
                lis.append(1)
                lis.append(1)
                return 0
            findKth(n-1)
            arr = lis[::]
            lis.append(1)
            lis.extend(reverse(arr))
            
        findKth(n)
        return str(lis[k-1])