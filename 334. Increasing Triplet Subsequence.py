import sys
class Solution(object):
    k = 3
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < self.k:
            return False
        increase_list = [sys.maxint] * self.k

        for i in xrange(len(nums)):
            j = 0
            while j < self.k-1 and nums[i] > increase_list[j]:
                j += 1
            if j == self.k - 1:
                return True
            if nums[i] < increase_list[j]:
                increase_list[j] = nums[i]
        return False

    def increasingTriplet2(self, nums):
        if len(nums) < 3:
            return False
        first, second = nums[0], sys.maxint
        for i in xrange(1, len(nums)):
            if nums[i] > second:
                return True
            elif nums[i] < second and nums[i] > first:
                second = nums[i]
            elif nums[i] < first:
                first = nums[i]
        return False





s = Solution()
print s.increasingTriplet([1,2,3,4,5])
