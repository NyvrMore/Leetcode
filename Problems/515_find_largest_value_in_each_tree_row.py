"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        result = []
        if root is None:
            return result
        
        index = 0
        curr_level = [root]
        while curr_level:
            next_level = []
            for node in curr_level:
                if index in d:
                    d[index] = max(d[index], node.val)
                else:
                    d[index] = node.val       
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            index += 1
        
        for i in range(index):
            result.append(d[i])
        return result

"""
Explanation

We will use a dictionary to hold the max value at each level. We then traverse each level, similar to level order, and and we process each node on that level,
we update max if our new element > current max. We then append the the max at each level to result and return the result
"""