class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sets = set(nums)
        for i in nums:
            temp = [j for j in str(i)]
            m = temp[::-1]
            sets.add(int("".join(m)))
        return len(sets)
