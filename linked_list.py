from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value, position):
        node = Node(value)

        if self.size == 0:
            node.nextNode = None
            self.head = node
        else:
            prev = self.head
            temp = self.head
            counter = 0
            while counter != position:
                prev = temp
                temp = temp.nextNode
                counter += 1

            prev.nextNode = node
            node.nextNode = temp

        self.size += 1

    def delete(self, position):
        prev = self.head
        current = self.head
        counter = 0
        while counter != position:
            prev = current
            current = current.nextNode
            counter += 1

        prev.nextNode = current.nextNode
        self.size -= 1

    def select(self, position):
        counter = 0
        current = self.head
        while counter != position:
            current = current.nextNode
            counter += 1

        return current

    def replace(self, position, value):
        counter = 0
        current = self.head
        while counter != position:
            current = current.nextNode
            counter += 1

        current.value = value

    def size(self):
        return self.size

    def print_values(self):
        current = self.head
        for i in range(0, self.size):
            print current.value
            current = current.nextNode
