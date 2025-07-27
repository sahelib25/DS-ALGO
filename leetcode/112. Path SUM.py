# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,currentsum):
            if node is None:
                return False
        
            
            currentsum += node.val

            # check if its a leaf node
            if node.left is None and node.right is None:
                return currentsum == targetSum
            
            return dfs(node.left,currentsum) or dfs(node.right,currentsum)

        return dfs(root,0)
      

        
        
