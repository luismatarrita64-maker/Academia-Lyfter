class NodeT:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = NodeT(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = NodeT(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = NodeT(data)
            else:
                self._insert_recursive(current_node.right, data)

    def print_tree(self):
        result = self._inorder(self.root)
        print(result if result else "Empty tree")

    def _inorder(self, current_node):
        if current_node is None:
            return ""
        left = self._inorder(current_node.left)
        right = self._inorder(current_node.right)

        text = ""
        if left:
            text += left + " "
        text += str(current_node.data)
        if right:
            text += " " + right
        return text

t = BinaryTree()
for number in (5, 3, 8, 1, 4, 7, 9):
    t.insert(number)
t.print_tree()   