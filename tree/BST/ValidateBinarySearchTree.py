# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(node, lower, upper):
            if node == None:
                return True

            return (lower == None or node.val > lower) and \
                    (upper == None or node.val < upper) and \
                    isValid(node.left, lower, node.val) and \
                    isValid(node.right, node.val, upper)

        return isValid(root, None, None)