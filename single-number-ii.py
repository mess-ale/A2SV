class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []
        neg = 0
        for  i in range(len(nums)):
            if nums[i] < 0:
                neg += 1
                nums[i] = -1*nums[i]
                
            bn = bin(nums[i])[::-1]
            for j in range(len(bn)):
                if bn[j] =="b":
                    break
                    
                if j >= len(res):
                    res.append(int(bn[j]))
                
                else:
                    res[j] += int(bn[j])
        for i in range(len(res)):
            res[i] = str(res[i]%3)
        
        ans = res[::-1]
        if neg %3 ==1:
            return -int("".join(ans),2)
        return int("".join(ans),2)