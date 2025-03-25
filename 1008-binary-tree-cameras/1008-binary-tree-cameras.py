# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, float('inf')
            l = dfs(node.left)
            r = dfs(node.right)
            dp0 = l[1] + r[1]
            dp1 = min(l[2] + min(r[1], r[2]), r[2] + min(l[1], l[2]))
            dp2 = 1 + min(l) + min(r)
            return dp0, dp1, dp2

        return min(dfs(root)[1:])

        