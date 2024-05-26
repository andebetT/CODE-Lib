class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    # Check if the head is None
    if not head:
        return None

    # Create a dummy node to handle the case when the head needs to be removed
    dummy = ListNode(0)
    dummy.next = head

    # Iteratively remove nodes with the given value
    prev = dummy
    current = head
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return dummy.next


