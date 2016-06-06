class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:return 0
        not_hold_stock = [0] * len(prices)
        hold_stock = [0] * len(prices)

        hold_stock[0], hold_stock[1] = -prices[0], -prices[1] if -prices[1] > -prices[0] else -prices[0]
        not_hold_stock[0], not_hold_stock[1] = 0, prices[1] - prices[0] if (prices[1] - prices[0]) > 0 else 0
        for i in range(2, len(prices)):
            hold_stock[i] = max(hold_stock[i-1], not_hold_stock[i-2] - prices[i])
            not_hold_stock[i] = max(not_hold_stock[i-1], hold_stock[i-1] + prices[i])
        return not_hold_stock[i]

s = Solution()
l = [1,2,3,0,2]
print s.maxProfit(l)