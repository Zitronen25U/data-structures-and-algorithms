
import pytest
from fizz_buzz_tree.fizz_buzz_tree import breadth_first_fizzbuzz, Tree, Node


# if __name__ == "__main__":
#     one = Node(1)
#     two = Node(2)
#     three = Node(3)
#     four = Node(4)
#     five = Node(5)
#     six = Node(6)
#     seven = Node(7)
#     eight = Node(8)

#     """
#                 1
#             2          5
#         3      4     6 7 8
#     """
    
#     one.children = [two, five]
#     two.children = [three, four]
#     five.children = [six, seven, eight]
#     kt = Tree()
#     kt.root = one
#     bf_collection = breadth_first_fizzbuzz(kt)
#     print(bf_collection)