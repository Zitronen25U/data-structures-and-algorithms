class Hashtable:
    def __init__(self, size=1024):
        self._buckets = [None] * size


    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum *= 599

        index = sum % len(self._buckets)
        return index


    def add(self, key, value):
        index = self.hash(key)
        if not self._buckets[index]:
            self._buckets[index] = LinkedList()

        self._buckets[index].append([key, value])


    def get(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]

        if not bucket:
            return None

        current = bucket.head 

        while current:
            if current.value[0] == key:
                return current.value[1]

        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]

        if not bucket:
            return None

        if bucket.value == index:
            return True

        else:
            return False





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
