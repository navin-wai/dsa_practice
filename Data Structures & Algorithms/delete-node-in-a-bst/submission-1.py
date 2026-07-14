# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def min_val_node(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def remove(root , val):
            if not root:
                return None
            if root.val > val:
                root.left = remove(root.left , val)
            elif root.val < val:
                root.right = remove(root.right , val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_node = min_val_node(root.right)
                    root.val = min_node.val
                    root.right = remove(root.right , min_node.val)
            return root

        return remove(root , val)