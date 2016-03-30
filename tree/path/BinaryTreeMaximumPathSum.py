import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathToRoot(node, maxPath):
            if node == None:
                return 0

            left = maxPathToRoot(node.left, maxPath)
            right = maxPathToRoot(node.right, maxPath)
            toRoot = node.val + max(left, right)
            sum = node.val + left + right
            maxPath[0] = max(maxPath[0], sum)

            return max(0, toRoot)

        maxPath = [-sys.maxsize]
        maxPathToRoot(root, maxPath)

        return maxPath[0]

