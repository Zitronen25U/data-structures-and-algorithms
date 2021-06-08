class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
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




