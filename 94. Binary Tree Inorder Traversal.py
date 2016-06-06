# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        in_order_list = list()
        if root is None:
            return in_order_list

        stack = list()
        while root is not None or len(stack):
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                in_order_list.append(root.val)
                root = root.right
        return in_order_list