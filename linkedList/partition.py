class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

def partition(head, x):
    if not head:
        return None

    left = ListNode()
    right = ListNode()

    ltail = left
    rtail = right

    while head:
        if head.val < x:
            ltail.next = head
            ltail = ltail.next

        else:
            rtail = head
            rtail = rtail.next

        head = head.next

    ltail.next = right.next
    rtail.next = None

    return left.next

