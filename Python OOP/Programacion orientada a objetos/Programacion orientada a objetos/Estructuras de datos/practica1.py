class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("The stack is empty")
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.data

    def print_stack(self):
        current = self.top
        elements = ""
        while current is not None:
            elements += str(current.data)
            if current.next is not None:
                elements += " -> "
            current = current.next
        print("Top -> " + elements if elements else "Empty stack")


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()   
s.pop()
s.print_stack()   