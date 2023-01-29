#User function Template for python3

class Solution: 
    def select(self, arr, i):
        return arr
    
    def selectionSort(self, arr,n):
        i = 0
        while i < n:
            j = i+1
            while j < n:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1
        self.select(arr,0)
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends