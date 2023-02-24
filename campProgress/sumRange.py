class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        cur = 0
        self.result = [0]
        for i in nums:
            cur += i
            self.result.append(cur)
    def sumRange(self, left: int, right: int) -> int:
        return self.result[right+1]-self.result[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
