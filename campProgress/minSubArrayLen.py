class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        first = 0
        last = 0
        max_num = 1000000
        max_val = 0
        while last < len(nums) and max_val < target:
            max_val += nums[last]
            last += 1
        if max_val == target:
            max_num = last

        while last < len(nums):
            while max_val >= target:
                max_val -= nums[first]
                first += 1
            print(last-first+1)
            max_val += nums[last]
            max_num = min(max_num, last-first+1)
            last += 1

        while max_val >= target:
            max_val -= nums[first]
            first += 1
            max_num = min(max_num, last-first+1)
        if max_num == 1000000:
            return 0
        return max_num
