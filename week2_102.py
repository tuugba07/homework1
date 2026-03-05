class Node():
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, text: str, value: int):
        """This methods uses text and value to construct binary tree
        text: this parameter will be used as a key 
        value: this parameter will be used as a position of the Node
        """
        self.root = Node(text, value)

    def add_node(self, text: str, value: int):
        """"Insert a Node which used as a BST.
        ıf a node can move to the right or left of the main root, it will; otherwise, it will be added there.
        text: this parameter will be used as a key
        value : this parameter will be used as a position of the Node 
        """
        new_node = Node(text, value)
        current_node = self.root

        while True:
            if value > current_node.value:  # eğer değeri büyükse sağa git
                if current_node.right is None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right
            elif value < current_node.value:  # Eğer değeri küçükse sola git
                if current_node.left is None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            else:
                break  # aynı değer varsa çık

    def add_note_alternative(self, text, value):
        new_node = Node(text, value)
        current_node = self.root
        while True:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            else:
                break  # aynı değer varsa çık

    def search_value(self, value: int):
        """searches for a node in BST and returns an error if none exist.
        ıt will return an error is the value is less than or greater than the leaf value.
        ıf it is equal to the node, it  will return the node's text.
        
        value: This parameter is used to find the text of the Node inside the BST.
        """   
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return current_node.key  # burda text yani key döndürülüyor
            elif current_node.value < value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return "Value not found"  # eğer değer bulunmazsa

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

    def delete(self, value: int):
        """Verilen value'ya sahip düğümü BST'den siler."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value: int):
        # Düğüm yoksa
        if node is None:
            return None

        # Aranan değer şu anki düğümden küçük -> sola git
        if value < node.value:
            node.left = self._delete(node.left, value)
            return node

        # Aranan değer şu anki düğümden büyük -> sağa git
        if value > node.value:
            node.right = self._delete(node.right, value)
            return node

        # Buraya geldiysek: node.value == value, yani silinecek düğümü bulduk

        # 1) Hiç çocuğu yoksa (yaprak düğüm)
        if node.left is None and node.right is None:
            return None

        # 2) Sadece sağ çocuğu varsa
        if node.left is None:
            return node.right

        # 3) Sadece sol çocuğu varsa
        if node.right is None:
            return node.left

        # 4) İki çocuğu varsa:
        # Sağ alt ağaçtaki en küçük düğümü (inorder successor) bul
        successor = self._min_node(node.right)
        # Bulduğumuz halefin (successor) value ve key'ini buraya kopyala
        node.value = successor.value
        node.key = successor.key
        # Aynı değere sahip düğümü sağ alt ağaçtan sil
        node.right = self._delete(node.right, successor.value)
        return node

    def _min_node(self, node):
        """Verilen alt ağaçtaki en küçük value'ya sahip düğümü döndürür."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min(self):
        """Ağaçtaki en küçük value'ya sahip düğümün key ve value'sunu döndürür."""
        if self.root is None:
            return None  # veya hata fırlatılabilir
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key, current.value

    def find_max(self):
        """Ağaçtaki en büyük value'ya sahip düğümün key ve value'sunu döndürür."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key, current.value

my_tree = BinaryTree("Mehmet", 32)
my_tree.add_node("Sabriye", 9)
my_tree.add_node("Emirhan", 31)
my_tree.add_node("Ata", 41)
my_tree.add_node("Burdur", 15)

print(my_tree.search_value(41))
print(my_tree.size())
print(my_tree.height())
print("Min:", my_tree.find_min())
print("Max:", my_tree.find_max())
