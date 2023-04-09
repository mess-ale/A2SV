class Solution:
    def countArrangement(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append(i+1)

        def permituation(arr, lists):
            if len(arr) == n:
                return 1
            
            if arr and not (((len(arr)+1) % arr[-1] == 0) or (arr[-1] % (len(arr)+1)) == 0):
                return 0
            
            count = 0
            for i in lists:
                if i not in arr:
                    arr.append(i)
                    count += permituation(arr, lists)
                    arr.pop()
            return count
            
        return permituation([], arr)