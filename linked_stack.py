from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        n = Node(val)
        n.nextNode = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            return None

        item = self.top
        self.top = self.top.nextNode
        return item.value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value
