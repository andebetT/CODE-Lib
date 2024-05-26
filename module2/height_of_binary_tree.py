#this program is used to find height of binary tree or max depth of binary tree
def height_of_binary_tree(a):
    if not a:
        return 0
    left_height=height_of_binary_tree(a.left)
    right_height=height_of_binary_tree(a.right)
    return 1+max(left_height,right_height)