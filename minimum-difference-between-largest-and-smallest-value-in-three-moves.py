class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0

        if nums[-1]-nums[3] < nums[-4]-nums[0]:
            return nums[-1]-nums[3]
            
        return nums[-4]-nums[0]