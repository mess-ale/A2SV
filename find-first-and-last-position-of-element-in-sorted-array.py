class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0,0]

        lis = [-1,-1]
        mid = 0
        def biscet_left(nums):
            low = 0
            high = len(nums)-1
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] < target:
                    low = mid+1

                else:
                    high = mid-1
                    
            return low

        def biscet_right(nums):
            low = 0
            high = len(nums)-1
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] <= target:
                    low = mid+1

                else:
                    high = mid-1
                    
            return high        

        first = biscet_left(nums)
        second = biscet_right(nums)
        if 0 <= first <= len(nums)-1 and nums[first] == target:
            lis[0] = first

        if 0 <= second <= len(nums)-1 and nums[second] == target:
            lis[1] = second
        return lis