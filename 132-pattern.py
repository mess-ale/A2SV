class Solution:  
    def find132pattern(self, nums: List[int]) -> bool:
        left = []
        for i in nums:
            if (not left) or (i <= left[-1]):
                left.append(i)
            else:
                left.append(left[-1])
        right = []
        temp = []
        for i in nums[::-1]:
            ind = bisect_left(temp, i)
            temp.insert(ind, i)
            if ind - 1 >= 0:
                right.append(temp[ind - 1])
            else:
                right.append(i)
        right = right[::-1]
        for i in range(1, len(nums) - 1):
            if (left[i - 1] < right[i]) and (nums[i] > right[i]):
                return True
        return False