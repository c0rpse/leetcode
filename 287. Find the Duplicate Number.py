class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast



s = Solution()
l = [1,1]
print s.findDuplicate(l)


