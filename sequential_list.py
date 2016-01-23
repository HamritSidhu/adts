from node import Node


class SequentialList:
    def __init__(self, list_size):
        self.size = 0
        self.elements = [None] * list_size

    def insert(self, value, position):
        node = Node(value)
        temp_array = self.elements[position:self.size+1]
        self.elements[position] = node

        for i in range(0, len(temp_array)):
            self.elements[position + i + 1] = temp_array[i]

        self.size += 1

    def delete(self, position):
        temp_array = self.elements[position+1:self.size+1]

        for i in range(0, len(temp_array)):
            self.elements[position + i] = temp_array[i]

        self.size -= 1

    def select(self, position):
        return self.elements[position]

    def replace(self, position, value):
        self.elements[position] = value

    def size(self):
        return self.size

    def print_values(self):
        for i in range(0, self.size):
            print self.elements[i].value
