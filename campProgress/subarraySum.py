class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixsum = [0]
        cur = 0
        answer = 0
        for i, num in enumerate(nums):
            cur += num
            prefixsum.append(cur)

        dec = defaultdict(int)
        for i in prefixsum:
            var = i - k
            answer += dec[var]
            dec[i] += 1
        return answer
