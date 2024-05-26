class BST:
    def __init__(self, key=None):
        self.key = key
        self.lchild = None
        self.rchild = None

    # insertion opration
    def insertion_opration(self, data):
        if self.key is None:
            self.key = data
            return
        elif self.key > data:
            if self.lchild is not None:
                self.lchild.insertion_opration(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.insertion_opration(data)
            else:
                self.rchild = BST(data)

    # searching opration in binary search tree
    def searching_element(self, data):
        if self.key == data:
            print("yes the data is peresent")
        elif self.key > data:
            if self.lchild is not None:
                self.lchild.searching_element(data)
            else:
                print("the node is not present in the tree")
        else:
            if self.rchild is not None:
                self.lchild.searching_element(data)
            else:
                print("the node is not present in the tree")

    # pre order traversing
    def pre_order_traversing(self):
        print(self.key, end=" ")
        if self.lchild is not None:
            self.lchild.pre_order_traversing()
        if self.rchild is not None:
            self.rchild.pre_order_traversing()

    def inorder_traversing(self):
        if self.lchild is not None:
            self.lchild.inorder_traversing()
        print(self.key, end=" ")
        if self.rchild is not None:
            self.rchild.inorder_traversing()

    def post_order_traversing(self):
        if self.lchild is not None:
            self.lchild.inorder_traversing()
        elif self.rchild is not None:
            self.rchild.inorder_traversing()
        print(self.key, end=" ")

    # delating the node of tree
    def delating_node(self, data, value):
        if self.key is None:
            print("the tree is empty")
        if self.key > data:
            if self.lchild is not None:
                self.lchild = self.lchild.delating_node(data)
            else:
                print("the data is not found in  the tree")
        elif self.key < data:
            if self.rchild is not None:
                self.lchild = self.lchild.delating_node(data)
            else:
                print("the data is not found in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == value:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                return temp
            if self.rchild is None:
                temp = self.rchild
                if data == value:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return temp
            minimum = self.rchild
            while minimum.lchild is not None:
                minimum = minimum.lchild
            self.key = minimum.key
            self.rchild = self.rchild.delating_node(minimum.key, value)
            return self

    '''def tree_size(self):
        if self is None:
            return 0
        return 1+max(BST.tree_size(self.lchild)+BST.tree_size(self.rchild))'''

    def finding_minimum(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(current.key)

    def finding_max(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(current.key)


def finding_height(node):
    if node is None:
        return 0
    return 1 + max(finding_height(node.rchild), finding_height(node.rchild))


# this code is used for counting the number of nodes of the tree
def counting_node(node):
    if node is None:
        return 0
    return 1 + counting_node(node.lchild) + counting_node(node.rchild)


# cheking binary tree is bst
def cheek_bst(n):
    if n:
        if n.lchild and n.key < n.lchild.key:
            return False
        cheek_bst(n.lchild)
        if n.rchild and n.key > n.lchild.key:
            return False
        cheek_bst(n.rchild)
    return True


bst = BST(10)
l = [20, 30, 4, 1, 5, 6]
for i in l:
    bst.insertion_opration(i)
bst.searching_element(4)
print()
print("this the pre order traversing")
bst.pre_order_traversing()
print()
print("this the inorder traversing")
bst.inorder_traversing()
print()
print("this the post order traversing")
bst.post_order_traversing()
bst.delating_node(10, 10)
print()
bst.post_order_traversing()
print()
bst.finding_minimum()
bst.finding_max()
print(counting_node(bst))
print(finding_height(bst))
print(cheek_bst(bst))
# print(bst.tree_size())

