class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        s = []
        for i in nums:
            if i > 0:
                s.append(i)

        
        sets = list(set(s))
        sets.sort()
        if len(sets) == 0:
            return 1
        print(sets)
        for i in range(1, max(sets)):
            if i > len(sets):
                break
                
            if i < sets[i-1]:
                return i

        return max(sets)+1