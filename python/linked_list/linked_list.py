class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def valueFinder(self):
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next
        return values

    def __str__(self):
        values = ""
        current = self.head

        while current:
            values.join(current.value)
            current = current.next
        return values

