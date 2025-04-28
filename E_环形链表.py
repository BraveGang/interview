"""
给你一个链表的头节点 head ，判断链表中是否有环。

https://leetcode.cn/problems/linked-list-cycle/

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 哈希表法 来判断哈希表中数据是否重复
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    # 快慢指针法
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
