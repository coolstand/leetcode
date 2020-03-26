import os
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ReturnNode(object):
    def __init__(self, isB, depth):
        self.isB = isB
        self.depth = depth

class Solution(object):
    def isBST(self, root):
        if root == None:
            return ReturnNode(True, 0)

        left = self.isBST(root.left)
        right = self.isBST(root.right)

        depCom = abs(left.depth - right.depth)

        if left.isB == False or right.isB == False or depCom > 1:
            return ReturnNode(False, 0)
        
        return ReturnNode(True, max(left.depth, right.depth) + 1)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBST(root).isB

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    a = Solution()
    print (a.isBalanced(root))