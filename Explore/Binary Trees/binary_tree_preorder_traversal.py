"""
Given a binary tree, return the preorder traversal of its nodes' values.

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal_Iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []

        while stack:
            current = stack.pop()
            if current is not None:
                result.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
        return result
    
    def preorderTraversal_Recursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        return [root.val] + self.preorderTraversal_Recursion(root.left) + self.preorderTraversal_Recursion(root.right)
