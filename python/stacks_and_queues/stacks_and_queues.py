class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Stack:
  def __init__(self):
    self.top = None

  def push(self, value):
    self.top = Node(value, self.top)

  def pop(self):

    if not self.top:
      raise InvalidOperationError("Method not allowed on empty collection")

    val = self.top.value
    self.top = self.top.next
    return self.top.value


  def is_empty(self):
    return self.top is None


  def peek(self):
    if not self.top:
      raise InvalidOperationError("Method not allowed on empty collection")



class Queue():
    def __init__(self, value):
        self.front = None

    def enqueue(self, value):
        self.front = Node(value, self.front)

    def dequeue(self):
        pass
        # need to figure this out?

    def peek(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.front is None

