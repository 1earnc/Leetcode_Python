"""
Recursion
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur: return
            ans.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        ans = []
        dfs(root)
        return ans