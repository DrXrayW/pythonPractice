# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def getPathsOfSum(node, sum, curpath, paths):
            if node == None:
                return

            curpath.append(node.val)

            if node.left == None and node.right == None and node.val == sum:
                paths.append(list(curpath))
            else:
                getPathsOfSum(node.left, sum - node.val, curpath, paths)
                getPathsOfSum(node.right, sum - node.val, curpath, paths)
            curpath.pop()
            return

        res = []
        getPathsOfSum(root, sum, [], res)
        return res
        