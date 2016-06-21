class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 1:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] > nums[right]:
                if nums[mid] >= nums[left]:
                    if target > nums[mid] or target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target < nums[mid] or target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
        if left == right and nums[left] == target:
            return left
        return -1

s = Solution()
print s.search([5,1,3],0)



