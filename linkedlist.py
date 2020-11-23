from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = self.head
        self.length += 1

    def append(self, data):
        new_node = Node(data, None)
        if self.length != 0:
            self.tail._next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def delete_from_head(self):
        if self.length == 0:
            return
        popped = self.head._data
        self.head = self.head._next
        self.length -= 1
        return popped

    def delete_from_tail(self):
        if self.length == 0:
            return

        # define two tracker nodes
        current_node = self.head
        previous_node = current_node

        # iterate until the last tracker node is the tail
        while current_node._next is not None:
            previous_node = current_node
            current_node = current_node._next

        # set next for node before tail to none
        previous_node._next = None
        self.tail = previous_node
        self.length -= 1

    def find(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node._data == data:
                return True
            current_node = current_node._next

        return False

    def delete(self, data):
        if self.length == 0:
            return
        # define two tracker nodes
        current_node = self.head
        previous_node = current_node

        # iterate until the current node is equal to the requested deletion
        while current_node is not None:
            if current_node._data == data:
                self.length -= 1
                previous_node._next = current_node._next
                return
            previous_node = current_node
            current_node = current_node._next

    def reverse(self):
        reversed_list = LinkedList()
        current_node = self.head
        while current_node is not None:
            reversed_list.prepend(current_node._data)
            current_node = current_node._next

        return reversed_list

    def get_length(self):
      return self.length

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node._data)
            current_node = current_node._next
        print('--------------')
