class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)

        self.invertTree(root.right)

        return root
