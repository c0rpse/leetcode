class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for v in nums:
            two |= one & v
            one ^= v
            three = ~(one & two)
            one &= three
            two &= three
        return one

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1,2,3,5,1,2,3,5,1,2,3,5,9])
