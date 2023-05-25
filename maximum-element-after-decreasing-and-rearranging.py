class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # arr = list(set(arr))
        arr.sort()
        arr[0] = 1

        for j in range(1, len(arr)):
            if abs(arr[j-1] - arr[j]) <= 1:
                continue
            else:
                arr[j] = arr[j-1] + 1

        print(arr)
        return max(arr)