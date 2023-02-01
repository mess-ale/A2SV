class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        goup = True
        godown = False
        i  = 0
        count = 0
        while i < len(arr)-1:
            if goup:
                if arr[i] < arr[i+1]:
                    count += 1
                    i += 1
                    continue
                else:
                    if arr[i] == arr[i+1]:
                        return False
                    if i+1 == len(arr):
                        return False
                    godown = True
                    goup = False
            elif godown:
                if arr[i] > arr[i+1]:
                    i += 1
                    continue
                else:
                    return False
        if godown and count >= 1:
            return True
        return False
