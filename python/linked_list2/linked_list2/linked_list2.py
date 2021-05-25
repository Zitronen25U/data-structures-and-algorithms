class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head


    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


   def insert(self, value):
        self.head = Node(value, self.head)


    def append(self, value):
      current = self.head
      while current:
        if current.next == None:
          current.next = Node(value)
          break
        current = current.next


    def valueFinder(self):
        current = self.head
        values = []

        while current:
            values.append(current.value)
            current = current.next
        return values


    def __str__(self):
        values = ""
        current = self.head

        while current:
            string = f'{current.value}  '
            current = current.next
        return values


    def insertBefore(self, value, newVal):
        current = self.head
        previous = None
        while current:
            if self.head == value:
                self.insert(newVal)
                break
            if current.value == value:
                previous.next = Node(newVal, current)
                break
            previous = current
            current = current.next

    def insertAfter(self, value, newVal):
        current = self.head
        insert_before_this = current.next
        while current:
            if self.head.value == value:
                self.insert_before(insert_before_this.value, newVal)
                break
            if current.value == value:
                current.next = Node(newVal, insert_before_this)
                break
            current = current.next
            insert_before_this = current.next





