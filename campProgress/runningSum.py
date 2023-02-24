class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            nums[i] = cur
        return nums
