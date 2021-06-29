from BinaryTree.tree import BinaryTree, Node

lst1= BinaryTree()
list2=BinaryTree()

def find_common_values(tree1, tree2):
    lst1 = tree1.pre_order_traversal()
    lst2 = tree2.pre_order_traversal()
    return [item for item in lst1 if item in list2]