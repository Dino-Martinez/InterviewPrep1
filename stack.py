from linkedlist import LinkedList

class Stack:
  def __init__(self):
    self._list = LinkedList()

  def push(self, data):
    self._list.prepend(data)

  def pop(self):
    return self._list.delete_from_head()

  def peek(self):
    return self._list.head._data

  def size(self):
    return self._list.get_length()

  