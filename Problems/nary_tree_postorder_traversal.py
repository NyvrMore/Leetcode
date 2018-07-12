"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        
        memo = {}
        stack = [root]
        while stack:
            curr = stack[-1]
            if curr.children == [] or curr in memo:
                node = stack.pop()
                result.append(node.val)
            else:
                for child in curr.children[::-1]:
                    stack.append(child)
                memo[curr] = True
        return result