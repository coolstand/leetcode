# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root
        
if __name__ == '__main__':
    root = TreeNode(3)
    left_1 = TreeNode(5)
    right_1 = TreeNode(1)
    root.left = left_1
    root.right = right_1
    left_2 = TreeNode(6)
    right_2 = TreeNode(2)
    left_1.left = left_2
    left_1.right = right_2
    left_3 = TreeNode(0)
    right_3 = TreeNode(8)
    right_1.left = left_3
    right_1.right = right_3
    left_4 = TreeNode(7)
    right_4 = TreeNode(4)
    right_2.left = left_4
    right_2.right = right_4

    a = Solution()
    result = a.lowestCommonAncestor(root, left_1, right_4)
    if result:
        print (result.val)
    else:
        print ("errrrr")
    
