class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @lru_cache(None)
        def helper(i, buy):
            if i == n: return 0

            ans = helper(i + 1, buy)
            if buy:
                ans = max(ans, helper(i + 1, False) - prices[i])
            else:
                ans = max(ans, helper(i + 1, True) + prices[i] - fee)
            return ans
        return helper(0, True)