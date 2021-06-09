from collections import deque


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        self.storage.pop()

    def peek(self):
        if self.storage:
            return self.storage[0]
        else:
            raise InvalidOperationError("method not allowed")

    def is_empty(self):
        if self.storeage:
            return len(self.storage) == 0
        else:
            raise InvalidOperationError("method not allowed")


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        root then left then right
        """

        def walk(root, collection):
            # base case
            if not root:
                return

            ## visit
            collection.append(root.value)

            # go left

            walk(root.left, collection)

            # go right

            walk(root.right, collection)

        collected_values = []

        walk(self.root, collected_values)

        return collected_values


    def in_order(self):
        def walk(root, collection):
            if not root:
                return

            walk(root.left, collection)
            walk(root.right, collection)
            collection.append(root.value)

        collected_values = []

        walk(self.root, collected_values)

        return collected_values



    def post_order(self):
        def walk(root, collection):
            if not root:
                return

            walk(root.left, collection)
            walk(root.right, collection)
            collection.append(root.value)

        collected_values = []
        walk(self.root, collected_values)
        return collected_values




    def find_maximum_value(self):
            def walk(root, collection):
                if not root:
                    return

                walk(root.left, collection)
                walk(root.right, collection)
                collection.append(root.value)

            collected_values = []

            walk(self.root, collected_values)

            max = 0

            for i in collected_values:
                if i > max:
                    max = i
            return max



    @staticmethod
    def breadth_first(tree):
        queue_breadth = Queue()
        queue_breadth.enqueue(tree.root)
        collection = []
        
        if not tree.root:
            return collection

        while not queue_breadth.is_empty():
            current = queue_breadth.dequeue()
            return collection.append(current.value)

            if current.left:
                queue_breadth.enqueue(current.left)
                

            if current.right:
                queue_breadth.enqueue(current.right)
            
            
        return collection

    




class BinarySearchTree(BinaryTree):
    def add(self,value):

        node = Node(value)

        def walk(root, node_to_add):
            if not root:
                return

            value_to_add = node_to_add.value

            if value_to_add < root.value:
                if root.left:
                    walk(root.left, node_to_add)
                else:
                    root.left = node_to_add

            else:
                if root.right:
                    walk(root.right, node_to_add)
                else:
                    root.rigth = node_to_add


        if not self.root:
            self.root = node
            return

        walk(self.root, node)




