class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0 
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            ans = max( ans, math.ceil(total_sum /(i + 1)))
        return ans