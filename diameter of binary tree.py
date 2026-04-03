class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def help(node):
            if not node:
                return 0
            lh=help(node.left)
            rh=help(node.right)
            self.diameter=max(self.diameter,lh+rh)
            return 1+max(lh,rh)
        help(root)
        return self.diameter
