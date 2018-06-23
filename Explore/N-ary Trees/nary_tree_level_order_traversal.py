"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result

        curr_level = [root]
        while curr_level:
            level_result = []
            next_level = []
            for node in curr_level:
                level_result.append(node.val)
                for child in node.children:
                    next_level.append(child)
            result.append(level_result)
            curr_level = next_level
        return result