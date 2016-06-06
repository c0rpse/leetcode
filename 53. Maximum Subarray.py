class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = None
        tmp_sum = None
        for i in xrange(len(nums)):

            tmp_sum = tmp_sum if max_sum + nums[i] < tmp_sum else tmp_sum+nums[i]
            if max_sum != None:
                max_sum = tmp_sum if tmp_sum > max_sum else max_sum
            else:
                max_sum = tmp_sum
        return max_sum

s = Solution()
print s.maxSubArray([1,3,2,1,4,5,6,7,11,-22,33,-45])