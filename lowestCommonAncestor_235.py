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
        if not root:
            return None
        root_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val > root_val and q_val > root_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
if __name__ == '__main__':
    root = TreeNode(6)
    left_1 = TreeNode(2)
    right_1 = TreeNode(8)
    root.left = left_1
    root.right = right_1
    left_2 = TreeNode(0)
    right_2 = TreeNode(4)
    left_1.left = left_2
    left_1.right = right_2
    left_3 = TreeNode(7)
    right_3 = TreeNode(9)
    right_1.left = left_3
    right_1.right = right_3
    left_4 = TreeNode(3)
    right_4 = TreeNode(5)
    right_2.left = left_4
    right_2.right = right_4

    a = Solution()
    result = a.lowestCommonAncestor(root, left_1, right_3)
    if result:
        print (result.val)
    else:
        print ("errrrr")
