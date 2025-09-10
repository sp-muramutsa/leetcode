# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        li = []

        def dfs(root):
            if root is None:
                return

            dfs(root.left)
            li.append(root)
            dfs(root.right)
        
        dfs(root)
        
        for i in range(len(li)):
            if li[i].val == p.val:
                if (i+1) == len(li):
                    return None

                return li[i+1]
