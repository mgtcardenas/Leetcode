# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1 # because there's always at least head
        node = head
        # 1. Iterate through the list to know the length
        while(node.next):
          length += 1
          node = node.next
        # 2. Divide the length with integer division 2 (//2)
        length //= 2
        node = head
        # 3. Iterate until the middle node and return it
        for i in range(length):
          node = node.next
        return node
