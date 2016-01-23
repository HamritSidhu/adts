from node import Node


class Queue:
    QUEUE_SIZE = 10

    def __init__(self):
        self.front = 0
        self.rear = 0
        self.elements = [None] * Queue.QUEUE_SIZE
        self.size = 0

    def enqueue(self, val):
        n = Node(val)
        self.elements[self.rear] = n
        self.rear = (self.rear + 1) % Queue.QUEUE_SIZE
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        item = self.elements[self.front]
        self.front = (self.front + 1) % Queue.QUEUE_SIZE
        self.size -= 1
        return item.value
