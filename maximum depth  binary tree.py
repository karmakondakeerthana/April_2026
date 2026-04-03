class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        c=0
        q=[root]
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            c+=1
        return c
