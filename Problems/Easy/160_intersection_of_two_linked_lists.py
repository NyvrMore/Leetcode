"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None
        
        pathA = headA
        pathB = headB
        
        while pathA is not pathB:
            pathA = headB if pathA is None else pathA.next
            pathB = headA if pathB is None else pathB.next
        return pathA

        """
        if pathA is None:
            pathA = headB
        else:
            pathA = pathA.next 
        """
        
"""
Explanation

If either of the heads are None, we return none.

If they're equal length, their intersection is easy to find. 

If not equal length, we traverse both paths until we hit the end and then start traversing the other respectively. This offsets the difference in length
and both will hit the intersection at the same time.


"""