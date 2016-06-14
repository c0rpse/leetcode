import copy


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        com = []
        ans = []
        if not n or not k:
            return com
        self.dfs(1, 0, n, k, ans, com)
        return com

    def dfs(self, start, num, n, k, ans, com):
        if num == k:
            print ans
            com.append(ans)
            return
        for index in xrange(start, n + 1):
            ans.append(index)
            self.dfs(index + 1, num + 1, n, k, ans, com)
            ans = ans[:-1]

s = Solution()
print s.combine(4, 2)




