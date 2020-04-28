import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        if left > right:
            return None
        pos = (left + right) // 2
        root = TreeNode(nums[pos])
        print (pos, nums[pos])
        root.left = self.helper(nums, left, pos-1)
        root.right = self.helper(nums, pos+1, right)
        return root


if __name__ == '__main__':
    a = Solution()
    root = a.sortedArrayToBST([-10,-3,0,5,9])
    result = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        length = len(queue)
        cur = []
        for _ in range(length):
            node = queue.popleft()
            cur.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(cur)
    print (result)
