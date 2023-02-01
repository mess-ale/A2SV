class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxs = arr[-1]
        i = len(arr)-2
        while i > 0:
            maxs = max(maxs, arr[i])
            arr[i] = maxs 
            i -= 1
        arr.append(-1)
        del arr[0]
        return arr
