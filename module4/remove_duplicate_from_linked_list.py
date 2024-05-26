def remove_duplicate(head):
    prev=None
    current=head
    d={}
    while current:
        if current.data in d:
            prev.next=current.next
            current=None
        else:
            d[current.data]=1
            prev=current
        current=prev.next
