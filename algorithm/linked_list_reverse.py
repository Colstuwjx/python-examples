# coding=utf-8

'''
Give listNode and make some linked lists
Reverse it.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    cur = head
    previous = None
    h = head
    while cur:
        h = cur
        exchange_node = cur.next
        cur.next = previous
        previous = cur
        cur = exchange_node
    return h


def recurseReverseLinkedList(head, new_head):
    '''
    每次需要遍历当前节点时，总需要回忆下一个节点是否为None
    如果不为None，需要把下一个节点记录下来成为新的head，并且把原值存成当前节点的next
    '''
    if head is None:
        return

    if head.next is None:
        # 终止
        new_head = head
    else:
        # 递归下一个节点
        new_head = recurseReverseLinkedList(head.next, new_head)
        head.next.next = head
        head.next = None
    return new_head


def main():
    # 1->2->3->4->None
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    head.next = p1
    p1.next = p2
    p2.next = p3

    # foreach and print.
    cur = head
    while cur is not None:
        print cur.val
        cur = cur.next

    # reverse to 4->3->2->1->None
    # new_head = reverseLinkedList(head)
    new_head = head
    new_head = recurseReverseLinkedList(head, new_head)

    # foreach and print.
    cur = new_head
    while cur is not None:
        print cur.val
        cur = cur.next


if __name__ == "__main__":
    main()
