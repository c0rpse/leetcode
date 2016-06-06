class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        curMin = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if price < curMin:
                curMin = price
            maxProfit = (price - curMin) if (price - curMin) > maxProfit else maxProfit
        return maxProfit