class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lis = []
        for i in range(0, len(nums)):
            if nums[i] == target:
                lis.append(i)
        return lis
