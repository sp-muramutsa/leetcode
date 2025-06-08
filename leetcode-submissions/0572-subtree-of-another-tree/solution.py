# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def level_order(queue):
            nodes = []
            while queue:
                children = []
                for node in queue:
                    nodes.append(node.val if node else None)
                    if node:
                        children.append(node.left)
                        children.append(node.right)

                queue = children

            return nodes

        p_list = level_order([p])
        q_list = level_order([q])

        return p_list == q_list

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.same = False

        def dfs(node):
            if not node:
                return

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    self.same = True

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.same

