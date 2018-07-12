"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root):
        if root is None:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        inorder = self.inorder(root)
        
        if len(inorder) == 0:
        	return True
        
        if len(inorder) == 1:
            return True
        print inorder
        for i in range(1, len(inorder)):
        	if not inorder[i] > inorder[i-1]:
        		return False
        return True
