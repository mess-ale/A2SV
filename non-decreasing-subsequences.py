class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(cur, start):
            if len(cur) > 1:
                res.add(tuple(cur))

            for i in range(start, len(nums)):
                if not cur:
                    dfs(cur + [nums[i]], i + 1)
                
                elif cur[-1] > nums[i]:
                    dfs(cur, i + 1)
                
                elif cur[-1] <= nums[i]:
                    dfs(cur + [nums[i]], i + 1)
        dfs([], 0)
        return list(res)