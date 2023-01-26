class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_num = 0
        i = 0
        j = len(height)-1
        while i < j:
            max_num = max(max_num, min(height[i],height[j])*abs(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_num