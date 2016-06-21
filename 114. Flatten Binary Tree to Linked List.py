# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not isinstance(root, TreeNode) or not root:
            return
        self.dfs_adjust(root)

    def dfs_adjust(self, root):
        if not root:
            return
        # print root.val
        if not root.left and not root.right:
            return root
        if root.left and not root.right:
            left = self.dfs_adjust(root.left)
            root.right = root.left
            root.left = None
            return left
        if not root.left and root.right:
            right = self.dfs_adjust(root.right)
            return right
        left = self.dfs_adjust(root.left)
        right = self.dfs_adjust(root.right)
        # print left.val, right.val
        left.right = root.right
        root.right = root.left
        root.left = None
        # print root.val
        return right
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
s.dfs_adjust(root)
while root:
    print root.val
    root = root.right





