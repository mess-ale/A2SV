class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for n in nums:
            if n in dict_:
                dict_[n] += 1
            else:
                dict_[n] = 1

        dict_ = {k: v for k, v in sorted(dict_.items(), key=lambda item: item[1], reverse=True)}
        return [n for n in dict_.keys()][:k]