"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''递归'''


def reverseList(self, head: ListNode) -> ListNode:

    # 递归终止条件
    if not head or not head.next:
        return head
    # 递归方法的调用
    new_head = self.reverseList(head.next)
    # 具体赋值逻辑
    head.next.next = head
    head.next = None
    
    return new_head


'''迭代'''

def reverseList2(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        node = curr.next
        curr.next = prev
        prev = curr
        curr = node
    return prev
