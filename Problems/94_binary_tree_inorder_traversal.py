"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal_Iterative(self, root):
    	"""
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root 
        stack, output = [], []
        done = False

        while not done:
            if current is not None:
                stack.append(current)
                current = current.left 
            else:
                if stack:
                    current = stack.pop()
                    output.append(current.val)
                    current = current.right 
                else:
                    done = True
        return output

    def inorderTraversal_Recursion(self, root):
    	"""
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        return self.inorderTraversal_Recursion(root.left) + [root.val] + self.inorderTraversal_Recursion(root.right)
        