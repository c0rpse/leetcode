# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if len(nums)
        return self.convert(nums, 0, len(nums)-1)

    def convert(self, nums, start, end):
        if start > end:
            return None
        mid = start + (end-start)//2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums, start, mid-1)
        root.right = self.convert(nums, mid+1, end)
        return root



s = Solution()
l = [1,3,4,5,6,11,32,45,999]
n = s.sortedArrayToBST(l)
print n.left.left


