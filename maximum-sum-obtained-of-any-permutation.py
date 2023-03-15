class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        ls = [0]*(len(nums)+1)
        for i,j in requests:
            ls[i] += 1
            ls[j+1] -= 1

        for i in range(1,len(ls)):
            ls[i] += ls[i-1]

        ls.pop()
        ls.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i,val in enumerate(ls):
            ans += nums[i]*val
                
        return ans%(10**9+7)