# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None or k < 1:
            return -1

        node_stack = list()
        while root is not None or len(node_stack):
            if root is not None:
                node_stack.append(root)
                root = root.left
            else:
                root = node_stack.pop()
                if k > 1:
                    k -= 1
                else:
                    return root.val
                root = root.right


class Inorder(object):
    in_list = list()

    def order(self,root):
        if root.left is not None:
            self.order(root.left)
        self.in_list.append(root.val)
        if root.right is not None:
            self.order(root.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    order = Inorder()
    order.order(root)
    print order.in_list


