class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, k = -1, -1, -1
        index, nums_len = 0, len(nums)
        while index < nums_len:
            if nums[index] == 0:
                i, j , k = i + 1, j + 1, k + 1
                nums[i], nums[j], nums[k] = 0, 1, 2

            elif nums[index] == 1:
                j, k = j + 1, k + 1
                nums[j], nums[k] = 1, 2
            else:
                k += 1
                nums[k] = 2

            index += 1
