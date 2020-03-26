# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''
    def compare(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        
        comp1 = compare(tree1.left, tree2.right)
        comp2 = compare(tree1.right, tree2.left)

        if comp1 and comp2 and tree1.val == tree2.val:
            return True

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return compare(root,root)
    '''
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list = []
        list.append(root)
        list.append(root)
        while len(list) > 0:
            t1 = list.pop()
            t2 = list.pop()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            list.append(t1.left)
            list.append(t2.right)
            list.append(t1.right)
            list.append(t2.left)
            
        return True

if __name__ == '__main__':
    list = [1,2,3,4,5,6]
    list.append(7)
    print (list)
    list.pop()
    print (list)
    list.pop()
    print (list)
