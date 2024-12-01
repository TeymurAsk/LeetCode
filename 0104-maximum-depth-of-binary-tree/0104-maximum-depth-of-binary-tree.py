class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        count+=1

        depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth +1