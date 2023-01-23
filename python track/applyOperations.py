class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        dic = []
        count = 0
        for i in range(0, len(nums)):
            print("overhere")
            if i + 1 <= len(nums) - 1:
                if nums[i] != 0 and nums[i] == nums[i + 1]:
                    dic.append(2 * nums[i])
                    nums[i + 1] = 0
                elif nums[i] == 0:
                    count += 1
                else:
                    dic.append(nums[i])

            else:
                if nums[i] != 0 and count + len(dic) < len(nums):
                    dic.append(nums[i])
                elif nums[i] == 0:
                    count += 1

        for i in range(count):
            dic.append(0)

        return dic