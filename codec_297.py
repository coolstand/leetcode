# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def reserialize(root, strRes):
            if root is None:
                strRes += "None,"
            else:
                strRes += str(root.val) + ","
                strRes = reserialize(root.left, strRes)
                strRes = reserialize(root.right, strRes)
            return strRes

        return reserialize(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            if l[0] == "None":
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)

            return root
        l = data.split(",")
        return rdeserialize(l)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    left_1 = TreeNode(2)
    right_1 = TreeNode(3)
    root.left = left_1
    root.right = right_1
    left_2 = TreeNode(4)
    right_2 = TreeNode(5)
    right_1.left = left_2
    right_1.right = right_2

    data = codec.serialize(root)
    print(data)
    root = codec.deserialize(data)
    print(root.val, root.left.val, root.right.val)
