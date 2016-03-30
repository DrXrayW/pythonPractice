# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.getDepth(root) == None:
            return False

        return True

    def getDepth(self, root):
        if root == None:
            return 0

        leftDepth = self.getDepth(root.left)
        if leftDepth == None:
            return None

        rightDepth = self.getDepth(root.right)
        if rightDepth == None:
            return None


        if abs(leftDepth - rightDepth) > 1:
            return None

        return max(leftDepth, rightDepth) + 1


        