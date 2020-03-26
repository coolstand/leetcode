# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
    '''
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        list = []
        list.append(root)
        while len(list) > 0:
            cur = list.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left != None:
                list.append(cur.left)
            if cur.right != None:
                list.append(cur.right)
        return root

if __name__ == '__main__':
    a = Solution()
    node = TreeNode(4)
    node.left = TreeNode(2)
    node.right = TreeNode(7)
    root = a.invertTree(node)
    print ("root:%d", root.val)
    print ("left:%d", root.left.val)
    print ("right:%d", root.right.val)
