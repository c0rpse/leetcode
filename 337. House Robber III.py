# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[0]

    def dfs(self,root):
        if not root:return 0, 0
        rob_left, no_rob_left = self.dfs(root.left)
        rob_right, no_rob_right = self.dfs(root.right)
        return max(no_rob_left + no_rob_right + root.val, rob_left + rob_right), rob_left + rob_right
