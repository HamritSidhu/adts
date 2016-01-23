from node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        n = Node(val)

        if self.head is None:
            self.tail = n
            self.head = self.tail
        else:
            self.tail.nextNode = n
            self.tail = n

    def dequeue(self):
        if self.head is None:
            return None

        item = self.head
        self.head = self.head.nextNode
        if self.head is None:
            self.tail = None

        return item.value
