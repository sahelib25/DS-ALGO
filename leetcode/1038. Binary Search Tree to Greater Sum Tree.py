# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # inorder traversal but traverse right node first
        greater_sum = 0
        def inorder(root):
            nonlocal greater_sum
            if root:
                inorder(root.right)
                # print(root.val, root.val + greater_sum)
                # current_node = root.val
                root.val += greater_sum
                greater_sum = root.val
                inorder(root.left) 
            
        inorder(root)
        return root
