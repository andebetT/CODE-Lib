def merge_linked_list(linked_list1, linked_list2):
    p = linked_list1
    q = linked_list2
    s = None
    if not q:
        return p
    if not p:
        return q
    if p and q:
        if p.val <= q.val:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
        new_head = s
    while p and q:
        if p.val <= q.val:
            s.next = p
            s = p
            p = p.next
        else:
            s.next = q
            s = q
            q = q.next
    if not p:
        s.next = q
    if not q:
        s.next = p
    return new_head