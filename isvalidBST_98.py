# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.prev = None

class Solution(object):
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.inorder(root)
        return res == list(sorted(res))
    
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    '''
    
    def isValidBST(self, root):
        return self.helper(root)
    
    def helper(self, root, lower = float("-inf"), upper = float("inf")):
        if not root:
            return True

        val = root.val
        if val <= lower or val >= upper:
            return False
        if not self.helper(root.left, lower, val):
            return False
        if not self.helper(root.right, val, upper):
            return False
        return True

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(1)
    right = TreeNode(5)
    root.left  = left
    root.right = right
    a = Solution()
    print (a.isValidBST(root))
