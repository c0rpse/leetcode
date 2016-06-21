class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = [''] * len(s)
        if not s or len(s) == 0:
            return ''
        left, right = 0, len(s) - 1
        while left < right:
            ret[left], ret[right] = s[right], s[left]
            left += 1
            right -= 1
        if left == right:
            ret[left] = s[left]
        return ''.join(ret)

s = Solution()
print s.reverseString('qwerty')


