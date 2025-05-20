class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root is None:
                return 0

            leftHeight = height(root.left)

            rightHeight = height(root.right)

            if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return height(root) >= 0
