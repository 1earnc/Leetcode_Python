"""
Recursion
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            ans.append(cur.val)
            dfs(cur.right)
        ans = []
        dfs(root)
        return ans