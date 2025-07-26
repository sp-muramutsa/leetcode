# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        path = []

        def dfs(node):
            if not node:
                path.append("None")
                return

            path.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ", ".join(path)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(", ")
        self.i = 0
        n = len(data)

        def helper():

            if self.i == n:
                return

            if data[self.i] == "None":
                self.i += 1
                return None
            else:
                root = TreeNode(int(data[self.i]))

            self.i += 1

            root.left = helper()
            root.right = helper()
            return root

        root = helper()
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

