class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find(nums, 0, len(nums) - 1)

    def find(self, nums, begin, end):
        if begin == end:
            return begin
        elif begin == end - 1:
            return begin if nums[begin] > nums[end] else end
        else:
            mid = begin + (end - begin) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                return self.find(nums, begin, mid - 1)
            else:
                return self.find(nums, mid + 1, end)







