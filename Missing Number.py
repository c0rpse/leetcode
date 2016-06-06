class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = len(nums)
        for i in xrange(ret):
            ret ^= i ^ nums[i]
        return ret

s =Solution()
print s.missingNumber([0])