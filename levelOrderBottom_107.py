# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, cur)
        
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    left_1 = TreeNode(9)
    right_1 = TreeNode(20)
    root.left = left_1
    root.right = right_1
    left_2 = TreeNode(15)
    right_2 = TreeNode(7)
    right_1.left = left_2
    right_1.right = right_2

    a = Solution()
    print (a.levelOrderBottom(root))
