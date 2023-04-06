class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxi = nums[0]
        for i in range(1,len(nums)):
            maxi |= nums[i]
            
        count = 0
        ln = 2**(len(nums))-1
        for i in range(1, ln+1):
            bn = bin(i)[::-1]
            tes = 0
            j = 0
            for i in range(len(nums)):
                if bn[j] == "b":
                    break

                else:
                    tes |= (nums[i]*int(bn[j]))
                    j += 1

            if tes == maxi:
                count += 1
        return count