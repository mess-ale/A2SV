class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        lis = []
        while first != last:
            if numbers[first] + numbers[last] < target:
                first += 1
            elif numbers[first] + numbers[last] > target:
                last -= 1
            else:
                lis.append(1 + first)
                lis.append(last + 1)
                return lis