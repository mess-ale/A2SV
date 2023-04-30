from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        l = SortedList()
        while nums:
            s = nums.pop()
            i = l.bisect_left(s)
            res.append(i)
            l.add(s)

        return res[::-1]