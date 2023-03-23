class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def val(arr, divisor):
            val = 0
            for i in arr:
                val += ceil(i/divisor)
            return val


        i = 1
        j = max(nums)
        while j > i:
            mid = i + (j - i)//2
            if val(nums, mid) > threshold:
                i = mid+1

            else:
                j = mid
                
        return i