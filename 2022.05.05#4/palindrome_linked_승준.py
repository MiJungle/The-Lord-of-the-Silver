from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = list()
        
        node = head
        
        while node is not None:
            res.append(node.val)
            node = node.next
            
        while len(res) > 1:
            if res.pop(0) != res.pop():
                return False
        
        return True