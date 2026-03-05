class Node:
    def __init__(self, text, value):
        self.text = text
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, text: str, value: int):
        self.root = Node(text,value)

    def add_node(self, text, value):  # <-- sadece bir self
        new_node = Node(text, value)
        current_node = self.root
        while True:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                print("ERROR: VALUE already exists!")
                return

    def delete_node(self, root, value):
        if root is None:
            return root

        # Arama kısmı
        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            # 1. Çocuk yoksa
            if root.left is None and root.right is None:
                return None

            # 2. Tek çocuk varsa
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # 3. İki çocuk varsa
            else:
                successor = self.find_min(root.right)
                root.value = successor.value
                root.right = self.delete_node(root.right, successor.value)

        return root

    def find_value(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return current_node.text
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return "ERROR: Not found"

    def size(self):
        return self._size(self.root)

    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, current_node):
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left), self._height(current_node.right))

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("   " * level + f"({node.text}, {node.value})")
        print_tree(node.left, level + 1)

class BST:
    def __init__(self):
        self.root = None

    def delete_node(self, root, value):
        if root is None:
            return root

        # Arama kısmı
        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            # 1. Çocuk yoksa
            if root.left is None and root.right is None:
                return None

            # 2. Tek çocuk varsa
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # 3. İki çocuk varsa
            else:
                successor = self.find_min(root.right)
                root.value = successor.value
                root.right = self.delete_node(root.right, successor.value)

        return root

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


                        
                












if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet",32)
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Emirhan",31)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Burdur",15)
    my_tree.add_node("Konya",42)
    my_tree.add_node("Bilecik",11)

    print_tree(my_tree.root)
    print(my_tree.find_value(41))
    print(my_tree.find_value(82))
    print(my_tree.size())
    print(my_tree.height())
    print("silmeden önce: ")
    print_tree(my_tree.root)

    my_tree.root=my_tree.delete_node(my_tree.root,11)
                                    

    print("silmeden sonra: ")
    print(my_tree.root)


def print_tree(node, level=0):
    if node is not None:
        # Önce sağ dalı yazdır
        print_tree(node.right, level + 1)
        # Sonra kendisini yazdır
        print("   " * level + f"({node.text}, {node.value})")
        # En son sol dalı yazdır
        print_tree(node.left, level + 1)

# Kullanım:
print_tree(my_tree.root)