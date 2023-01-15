class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        odd.sort()
        even.sort()
        for i in odd:
            even.append(i)
        return even
