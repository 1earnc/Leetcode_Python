"""
Recursion
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N):
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        ans = []
        for i in range(1, N, 2):        #From 1 to n-1, step = 2
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)      #set initial node
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans


if __name__ == '__main__':
    N = 7
    mm = Solution()
    print(mm.allPossibleFBT(N))