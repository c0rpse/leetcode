class Solution(object):
    p_list = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:return []
        if n == 1: return ['()']
        p_list = []
        for i in self.generateParenthesis(n-1):
            for j in range(len(i)-1):
                p_list.append(i[:j]+'()'+i[j:])
            p_list.append('('+i+')')
        return list(set(p_list))




s = Solution()
print s.generateParenthesis(3)




