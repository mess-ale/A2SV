class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum = sum(num for num in nums if num % 2 == 0)
        ans = []

        for i in range(len(nums)):
            val, id = queries[i]
            
            if nums[id]%2 == 0:
                even_sum -= nums[id]
            nums[id] += val
            if nums[id]%2 == 0:
                even_sum += nums[id]
            queries[i] =  even_sum
            

        return queries

