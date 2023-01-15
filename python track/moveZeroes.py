class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        m = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                stack.append(nums[i])
            else:
                m += 1
                
        for i in range(0, m):
            stack.append(0)
        
        for i in range(0, len(nums)):
            nums[i] = stack[i]
        
