class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] != i+1 and nums[i] < len(nums) and nums[i] >= 1 and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
            else:
                i += 1
        print nums
        for i in xrange(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return len(nums)+1



s = Solution()
l = [10001,9,-1]
print s.firstMissingPositive(l)