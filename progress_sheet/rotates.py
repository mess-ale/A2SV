class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            pass
        elif k > 0:
            if k > len(nums):
                s = k%len(nums)
            else:
                s = k
            index = len(nums)-(s)
            ls = []
            for i in range(index, len(nums)):
                ls.append(nums[i])
            for i in range(0, index+1):
                ls.append(nums[i])
            for i in range(0, len(nums)):
                nums[i] = ls[i]
