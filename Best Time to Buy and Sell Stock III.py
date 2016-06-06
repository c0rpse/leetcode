import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) < 2:
            return max_profit
        i_pre_max_profit = [0]*len(prices)
        i_post_max_profit = [0]*len(prices)

        cur_min = 0
        for i in xrange(len(prices)-1):
            if prices[i] < cur_min:
                cur_min = prices[i]
            i_pre_max_profit[i] = prices[i] - cur_min

        cur_max = prices[-1]
        for j in reversed(xrange(len(prices)-1)):
            if prices[j] > cur_max:
                cur_max = prices[j]
            if j < len(prices)-2:
                i_post_max_profit[j] = (cur_max - prices[j])

        for i in xrange(len(prices)-1):
            cur_max_profit = i_post_max_profit[i]+i_pre_max_profit[i]
            max_profit = cur_max_profit if cur_max_profit > max_profit else max_profit
        return max_profit


if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,2,1,3,4,2,1,2,4,5]
    m = s.maxProfit(l)
    print m


