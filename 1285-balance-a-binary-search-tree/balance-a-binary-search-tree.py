# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, arr, l, r):
        if l > r:
            return None
        m = (l + r) // 2
        root = TreeNode(arr[m])
        root.left = self.build(arr, l, m - 1)
        root.right = self.build(arr, m + 1, r)
        return root

    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        self.inorder(root, arr)
        result = self.build(arr, 0, len(arr) - 1)
        return result