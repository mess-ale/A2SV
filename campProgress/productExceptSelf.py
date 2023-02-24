class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        result = []
        count = 0
        val = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                cur *= nums[i]
                result.append(cur)
            else:
                count += 1
                val = i
                
        if count == 1:
            m = [0]*len(nums)
            m[val] = result[-1]
            return m
        elif count > 1:
            return [0]*len(nums)

        ls = []
        for i in range(len(nums)):
            ls.append(result[-1]//nums[i])
        return ls
            
