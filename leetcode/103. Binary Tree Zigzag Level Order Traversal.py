# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        level = 0

        while q:
            level_size = len(q)
            node_levels = []
            
            for _ in range(level_size):
                node = q.popleft()
                node_levels.append(node.val)
            
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                node_levels.reverse()
            
            res.append(node_levels)
            level += 1
        return res
