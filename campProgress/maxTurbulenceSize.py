class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        max_val = 0
        count = 0
        max_val1 = 0
        count1 = 0
        for i in range(len(arr)-1):
            if i % 2 == 0:
                if arr[i] < arr[i+1]:
                    count += 1
                    max_val = max(max_val, count)
                else:
                    count = 0
                if arr[i] > arr[i+1]:
                    count1 += 1
                    max_val1 = max(max_val1, count1)
                else:
                    count1 = 0
            else:
                if arr[i] > arr[i+1]:
                    count += 1
                    max_val = max(max_val, count)
                else:
                    count = 0
                if arr[i] < arr[i+1]:
                    count1 += 1
                    max_val1 = max(max_val1, count1)
                else:
                    count1 = 0

        return max(max_val+1, max_val1+1)
