def has_cycle(head) :
    if not head or not head . next:
        return False # No cycle with fewer than two nodes
    slow = head
    fast = head
    while fast and fast. next :
        slow = slow . next # Move one step
        fast = fast. next. next # Move two steps
        if slow == fast:
            return True # Cycle detected
    return False # No cycle found