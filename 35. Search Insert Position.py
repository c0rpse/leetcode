class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return 0
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        print nums[mid]
        return start if nums[mid] < target else end + 1
s = Solution()
l = [1,4,5,7,8,9,10,22,34,55,99,103]
print s.searchInsert(l,33)