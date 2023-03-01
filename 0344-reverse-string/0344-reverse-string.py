class Solution:
    def reverseString(self, s: List[str]) -> None:
        arr = s[::]
        def reverse(s, m):
            nonlocal arr
            if m == len(s):
                return 0
            reverse(s, m+1)
            s[m], arr[len(s)-1-m] = arr[len(s)-1-m], s[m]

        reverse(s, 0)
