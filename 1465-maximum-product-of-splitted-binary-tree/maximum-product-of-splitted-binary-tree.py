# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 0
        root.val += self.dfs(root.left) + self.dfs(root.right)
        return root.val

    def solve(self, root, res, total):
        if not root:
            return
        prod = root.val * (total - root.val)
        res[0] = max(res[0], prod)
        self.solve(root.left, res, total)
        self.solve(root.right, res, total)
        return

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        total = root.val
        res = [0]
        self.solve(root, res, total)
        return res[0] % 1000000007
