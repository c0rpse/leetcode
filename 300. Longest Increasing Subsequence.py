class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        long_list, max_length = [1] * len(nums), 1
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j] and long_list[i] < long_list[j] + 1:
                    long_list[i] = long_list[j] + 1
                    if long_list[i] > max_length:
                        max_length = long_list[i]
        return max_length

s = Solution()
l= [10,9,2,5,3,7,101,18]
print s.lengthOfLIS(l)