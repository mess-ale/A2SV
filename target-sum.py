class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if nums[0] != 0:
            dp = {nums[0]: 1, -nums[0]: 1}
        if nums[0] == 0:
            dp = {0:2}

        for i in range(1, len(nums)):
            temp = {}
            for key in dp:
                temp[key + nums[i]] = temp.get(key + nums[i], 0) + dp[key]
                temp[key - nums[i]] = temp.get(key - nums[i], 0) + dp[key]
            dp = temp
            
        return dp.get(target, 0)