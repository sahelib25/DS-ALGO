# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def range_sum(root):
            if not root:
                return

            nonlocal summ
            # PreOrder 
            if root.val >= low and root.val<= high:
                summ += root.val
            if root.val>= low:
                range_sum(root.left)
            if root.val<= high:
                range_sum(root.right)
            return summ

        return range_sum(root)
            
