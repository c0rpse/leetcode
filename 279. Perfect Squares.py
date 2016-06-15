class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i for i in xrange(n + 1)]
        for i in xrange(n + 1):
            j = 1
            while i + j**2 <= n:
                squares[i + j**2] = min(squares[i] + 1, squares[i + j**2])
                j += 1
        return squares[n]
