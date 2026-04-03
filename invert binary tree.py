class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        root.left,root.right=root.right,root.left
        l=self.invertTree(root.left)
        r=self.invertTree(root.right)
        return root
