# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val = root.val
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        
        return 
    
    def rob(self, root):
        dic = {}
        def helper(root, dic):
            if not root:
                return 0
            if dic.get(root):
                return dic[root]
            val = root.val

            if root.left:
                val += helper(root.left.left, dic) + helper(root.left.right, dic)
            
            if root.right:
                val += helper(root.right.left, dic) + helper(root.right.right, dic)
            dic[root] = max(val, helper(root.left, dic) + helper(root.right, dic))
            return dic[root]
        
        return helper(root, dic)
    '''
    def rob(self, root):
        def helper(root):
            if not root:
                return [0,0]
            result = [0,0]
            left = helper(root.left)
            right = helper(root.right)

            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            result[1] = left[0] + right[0] + root.val
            return result

        result = helper(root)
        return max(result[0], result[1])



if __name__ == '__main__':
    a = Solution()
    root = TreeNode(3)
    left_1 = TreeNode(2)
    right_1 = TreeNode(3)
    root.left = left_1
    root.right = right_1
    right_2 = TreeNode(3)
    left_1.right = right_2
    right_3 = TreeNode(1)
    right_1.right = right_3

    data = a.rob(root)
    print(data)
