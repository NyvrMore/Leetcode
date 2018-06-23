"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal_Iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        prev = None 
        current = root
        while stack or current is not None:
            if current is not None:
                # Add all left nodes to stack
                stack.append(current)
                current = current.left
            else:
                # Peek to get the parent node
                peek = stack[-1]
                # Consider right nodes: peek must not be None and must not be a node we've previously added
                if peek.right is not None and prev is not peek.right:
                    current = peek.right
                else:
                    result.append(peek.val)
                    prev = stack.pop()
        return result

    def postorderTraversal_Recursion(self, root):
        # Recursion
        if root is None:
            return []
        
        return self.postorderTraversal_Recursion(root.left) + self.postorderTraversal_Recursion(root.right) + [root.val] 
