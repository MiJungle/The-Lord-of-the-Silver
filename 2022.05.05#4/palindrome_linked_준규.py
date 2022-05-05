# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        link = head
        arr = []
        while(link):
            arr.append(link.val)
            link = link.next
        left = 0
        right = len(arr) - 1
        while(left<right):
            if (arr[left] != arr[right]):
                return False
            left +=1
            right -=1
        return True
            
            
