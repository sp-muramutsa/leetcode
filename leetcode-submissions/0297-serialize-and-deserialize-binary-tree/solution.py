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

        traversal = []

        def dfs(node):
            if not node:
                traversal.append("None")
                return

            traversal.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(traversal)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")
        n = len(data)
        i = 0
        print(data)

        def dfs():

            nonlocal i
            if i == n:
                return

            if data[i] == "None":
                i += 1
                return None
            else:
                node = TreeNode(int(data[i]))

            i += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

