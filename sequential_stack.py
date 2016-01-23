from node import Node


class Stack:
    STACK_SIZE = 10

    def __init__(self):
        self.top = -1
        self.elements = [None]*self.STACK_SIZE

    def push(self, val):
        self.top += 1
        n = Node(val)
        self.elements[self.top] = n

    def pop(self):
        if self.top == -1:
            return None

        item = self.elements[self.top]
        self.top -= 1
        return item.value

    def peek(self):
        if self.top > -1:
            return self.elements[self.top].value
        return None
