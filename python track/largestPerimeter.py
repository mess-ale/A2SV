class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        answ = []
        for i in range(len(nums)-1, 0, -1):
            if i < 2:
                break   
            if nums[i] < nums[i-2] + nums[i-1]:
                answ.append(nums[i])
                answ.append(nums[i-1])
                answ.append(nums[i-2])
                break
            else:
                continue
                
        return sum(answ)
