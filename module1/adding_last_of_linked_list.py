#this program is used for adding elements to the last of linked list with constant space
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head

        if current is None:
            print("LinkedList is empty")
            return

        while current:
            print(current.data, end=" ")
            current = current.next

# Create a new linked list
my_list = LinkedList()

# Add nodes to the linked list
my_list.add_node(10)
my_list.add_node(20)
my_list.add_node(30)
my_list.add_node(40)

# Display the linked list
my_list.display()