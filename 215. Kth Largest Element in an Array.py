class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in xrange(k):
            cur_max = 0
            for j in xrange(1, len(nums) - i):
                if nums[j] > nums[cur_max]:
                    cur_max = j
            tmp = nums[cur_max]
            nums[cur_max] = nums[-i-1]
            nums[-i-1] = tmp
        return nums[-k]

s = Solution()
print s.findKthLargest([3,2,1,5,6,4],2)
