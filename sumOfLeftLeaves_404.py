# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    result = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and ( root.left.left is None and root.left.right is None):
            self.result += root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.result

if __name__ == '__main__':
    a = Solution()
    root = TreeNode(3)
    node_left_1 = TreeNode(9)
    node_right_1 = TreeNode(20)
    root.left = node_left_1
    root.right = node_right_1
    node_left_2 = TreeNode(15)
    node_right_2 = TreeNode(7)
    node_right_1.left = node_left_2
    node_right_1.right = node_right_2
    print (a.sumOfLeftLeaves(root))
