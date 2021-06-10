class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self):
        self.root = None


def breadth_first_fizzbuzz(tree):
    # if there is nothing
    if tree.root is None:
        return
    # Create an empty queue
    q = []
    # Enqueue Root
    q.append(tree.root)
    # while there are things in the queue loop
    # while (len(q) > 0):

    new_tree = Tree()

    while q:
        # do stuff
        fizzbuzz_value = fizzbuzz(q[0].value)
        print(fizzbuzz_value)
        node = q.pop(0)
        # Enqueue each child
        for child in node.children:
            q.append(child)


def fizzbuzz(root_value):
    # Number divisible by 15,(divisible
    # by both 3 & 5), print 'FizzBuzz'
    # in place of the number
    if root_value % 15 == 0:
        root_value = "FizzBuzz"
        return root_value
    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif root_value % 3 == 0:    
        root_value = "Fizz"
        return root_value
    # Number divisible by 5,
    # print 'Buzz' in
    # place of the number
    elif root_value % 5 == 0:        
        root_value = "Buzz"
        return root_value
    return str(root_value)


def make_new_tree(fizzbuzz):
    pass




