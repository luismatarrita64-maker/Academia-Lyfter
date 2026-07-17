class NodeD:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = NodeD(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = NodeD(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("The deque is empty")
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None  
        return removed_node.data

    def pop_right(self):
        if self.tail is None:
            print("The deque is empty")
            return None
        removed_node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None  
        return removed_node.data

    def print_deque(self):
        current = self.head
        elements = ""
        while current is not None:
            elements += str(current.data)
            if current.next is not None:
                elements += " <-> "
            current = current.next
        print("Head -> " + elements + " <- Tail" if elements else "Empty deque")


d = Deque()
d.push_right(2)
d.push_right(3)
d.push_left(1)
d.print_deque()   
d.pop_left()
d.pop_right()
d.print_deque()   