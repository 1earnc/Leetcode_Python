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
            dfs(cur.right)
            dfs(cur.left)
            ans.append(cur.val)
        ans = []
        dfs(root)
        return ans