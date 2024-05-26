#creating node
class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

        #nref means next node reference
        #pref means previous node reference
#create double linked list
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def traversal_opration_forward(self):
        if self.head is None:
            print("linked list is empty")
            return
        n=self.head
        while n is not None:
            print(n.data)
            n=n.nref
    def backward_traversing(self):
        if self.head == None:
            print("the linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n=n.pref
    def adding_to_emptylinked_list(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            return
        print("the linked list is not empty")
    def adding_bigining_ll(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def adding_end(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head=new_node

        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            new_node = Node(data)
            n.nref=new_node
            new_node.pref=n
    def adding_after_given_node(self,data,x):
        if self.head is None:
            print("the linked is empty we cannot add")
        else:
            n=self.head
            while n is not None:
                n=n.nref
                if n.data==x:
                    new_node = Node(data)
                    n.nref=new_node
                    new_node.nref=n.nref
    def deleting_first_node(self):
        if self.head is None:
            print("the linked listis empty we canot delate")
        else:
            self.head=self.head.nref
    def delating_end(self):
        n=self.head
        while n.nref.nref is not None:
            n=n.nref
        n.nref=None


    def adding_after(self,data,value):
        n=self.head
        if n.data==value:
            new_node=Node(data)
            new_node.nref=n.nref
            n.nref=new_node
    def adding_before(self,data, value):
        n=self.head
        while n is not None:
            if n.nref.data==value:
                new_node=Node(data)
                n.nref=new_node
                new_node.nref=n.nref
                n.pref=new_node





doble=DoubleLinkedList()
doble.adding_to_emptylinked_list(10)
doble.adding_bigining_ll(1000)
doble.adding_bigining_ll(2000)
doble.adding_end(3000)
doble.adding_after(5000,2000)
doble.adding_before(6000,5000)
doble.backward_traversing()
doble.deleting_first_node()
doble.delating_end()
doble.traversal_opration_forward()