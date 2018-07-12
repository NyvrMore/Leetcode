"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        curr = head
        while curr is not None:
            if curr.val is not None:
                curr.val = None
            else:
                return True
            curr = curr.next
        return False


"""
Explanation

We change the value to some unique value (in this case, None). We then keep looping through until we hit the end of the list
or the value of a given node is none. The former means no cycle while the latter indicates a cycle.

"""