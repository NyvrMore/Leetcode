"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""

class MapNode(object):
    
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = MapNode()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = MapNode()
            node = node.children[c]
        node.value = val
        
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        node = self.root
        for c in prefix:
            if c not in node.children:
                return total
            node = node.children[c]
        total += node.value # consider current node
        
        queue = [node for key, node in node.children.iteritems()]

        while queue: # not empty
            node = queue.pop()
            total += node.value
            queue = [node for key, node in node.children.iteritems()] + queue

        return total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)