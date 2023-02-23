class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums)/k
        win = sum(nums[:k])
        max_num = win
        for i in range(k,len(nums)):
            win += nums[i]
            win -= nums[i-k]
            max_num = max(max_num, win)
        return max_num/k
