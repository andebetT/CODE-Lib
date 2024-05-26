#creatung node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def traversing(self):
        if self.head==None:
            print("the linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def adding_bigin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def adding_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,target):
        n=self.head
        while n is not None:
            if target==n.data:
                break
            n=n.ref
        if n is None:
            print("the element is not found in the linked list")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref = new_node
    def add_before(self,data,target):
        if self.head is None:
            print("the linked list is empty ")
            return
        n=self.head
        if target==n.data:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==target:
                break
            n=n.ref
        new_node=Node(data)
        new_node.ref=n.ref
        n.ref=new_node

#inserting an element if the linked list is empty
    def adding_to_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("the linked is not empty")
    #deleting the first element of linked list
    def delate_first(self):
        if self.head is None:
            print("the linked list is empty and cannot delate")
        n=self.head
        self.head=self.head.ref
    #delating last node
    def delate_last(self):
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None
    #delating any element of the linked list by value
    def delate_by_value(self,value):
        n=self.head
        if n is None:
            print("the linked list is empty we cannot delete")
        if n.data==value:
            n=n.ref
            return
        while n.ref is not None:
            if n.ref.data==value:
                break
            n = n.ref
        if n.ref is None:
            print("print the node is not found")
            return
        n.ref=n.ref.ref

        # Function to reverse the linked list
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.ref
            current.ref = prev
            prev = current
            current = next
        self.head = prev
    def middle_linked_list(self):
        slow=self.head
        fast=self.head
        while fast and fast.ref:
            fast=fast.ref.ref
            slow=slow.ref
        return slow
    def delate_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.ref:
            fast = fast.ref.ref
            slow = slow.ref
            if slow.ref is None:
                self.head.ref=None
                return self
        slow.data=slow.ref.data
        slow.ref=slow.ref.ref
        return self
    def swap_linkedlist_elements(self,key1,key2):
        prev=None
        current=self.head
        while current and current.data!=key1:
            prev=current
            current=current.ref
        #print(prev.data)
        #print(current.data)
    def finding_length(self):
        current=self.head
        length=0
        while current:
            length+=1
            current=current.ref
        return length
    def merge_two_sorted_linked_list(self,linked):
        p=self.head
        q=linked.head
        s=None
        merged_node=None
        if not q:
            return p
        if not p:
            return q
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.ref
            else:
                s=q
                q=s.ref
            merged_node=s
        while p and q:
            if p.data<=q.data:
                s.ref=p
                s=p
                p=s.ref
            else:
                s.ref=q
                s=q
                q=s.ref
        if not q:
            s.ref=p
        if not p:
            s.ref=q
        return merged_node
    #method
    def remove_duplicate(self):
        prev=None
        current=self.head
        d={}
        while current:
            if current.data in d:
                prev.ref=current.ref
                current=None
            else:
                d[current.data]=1
                prev=current
            current=prev.ref
        return self













lin=LinkedList()
lin.adding_to_empty(150)
lin.adding_bigin(40)
lin.adding_end(200)
lin.adding_bigin(30)
lin.adding_bigin(30)
lin.adding_end(40)
#lin.add_after(1500,100)
#lin.adding_bigin(500)
#lin.add_before(900,1500)
#lin.delate_first()
#lin.delate_last()
#lin.delate_by_value(900)
#lin.traversing()
#lin.reverse_linked_list()
#lin.traversing()
#lin.middle_linked_list()
#lin.delate_middle_node()
#lin.traversing()
#lin.swap_linkedlist_elements(100,1000000)
#print(lin.finding_length())
print(lin.remove_duplicate())
lin2=LinkedList()
lin2.adding_to_empty(2500)
lin2.adding_bigin(50)
lin2.adding_end(2000)
lin2.adding_end(4000)
lin2.adding_bigin(40)
#lin2.traversing()
#print(lin.merge_two_sorted_linked_list(lin2.head))
#print(lin.remove_duplicate())
print(lin.traversing())


list=[[1,2],[3,4]]
print(sum(list,[]))