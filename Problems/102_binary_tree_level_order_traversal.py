"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        # curr_level is initated to level 0
        curr_level = [root]

        # For each level that's non-empty
        while curr_level:     
            level_result = [] # list of nodes for current level
            next_level = []  # list of nodes for next level
            for node in curr_level: # for each node in this level
                level_result.append(node.val) # append its value
                if node.left: # if left child exists, add it to next level
                    next_level.append(node.left)
                if node.right: # if right child exists, add it to next level
                    next_level.append(node.right)
            result.append(level_result) # appenn results with current level
            curr_level = next_level # set next level
        return result