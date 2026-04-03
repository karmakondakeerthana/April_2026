class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[(root,0,0)]
        colt=defaultdict(list)
        while q:
            node,row,col=q.pop(0)
            colt[col].append((row,node.val))
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        res=[]
        for col in sorted(colt.keys()):
            coln=sorted(colt[col],key=lambda x:(x[0],x[1]))
            res.append([val for row,val in coln])
        return res
