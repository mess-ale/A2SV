from sortedcontainers import SortedList
import numpy as np

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = np.array(nums1) - np.array(nums2)
        seen = SortedList()
        count = 0
        
        for n in nums:
            count += seen.bisect_right(n + diff)
            seen.add(n)
        
        return count