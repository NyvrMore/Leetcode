"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        if curr is None:
            return None
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

"""
Explanation

We start at the head and prev is initially none. If curr is none, we return None. Then while curr is not None, we let next be the next
node. Now that we have the next node, we set next to point to prev and then update prev to be the current node. We then move to the next node
we initally saved.

1. get next node
2. set next of current node
3. update prev node to curr
4. update curr node to next
"""