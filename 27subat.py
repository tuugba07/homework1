class Node():   #Node sınıfı ikili ağaçtaki tek bir sınıfı kabul edecek.
    def __init__(self,text,value):  #Sınıfın kurucu metodudur.İinit metodu sınıfta yeni bir nesne oluştuğunda otomatik çalışır.
        self.text=text    #text düğümün ismi(mehmet). value düğümün sayısal değeridir(78).
        self.value=value
        self.left=None       #başlangıçta sağda ve solda çocuk olmadığı için none atanır.binarytree sınıfı ile yeni çocuklar atanabilir.
        self.right=None

class BinaryTree():
    def __init__(self,text:str,value:int):  #init metodu çalıştığında verilen key ve value değerleri ile bir roof(kök) yapısı oluşur
        self.root=Node(text,value)    #sonradan eklenilen her düğüm(add_node)bu düğümün altına yerleşir.

    def add_node(self,text,value):
        new_node=Node(text,value)
        current_node = self.root   #current_node ağaç üzerinde dolaşırken o an üzerinde bulunduğun değeri tutar.
        while True:
            if value>current_node.value:   #yeni değer mevcut değerden büyükse sağa bakılır.
                if current_node.right is None:   #eğer mevcut düğümün sağ çocuğu yoksa buraya eklenir.
                    current_node.right = new_node   #artık ağaçta yerini buldu.
                    break
                else:    #sağ taraf dolusa çalışır.
                    current_node=current_node.right
            elif value<current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                break
            else:
                current_node = current_node.left
        else:
            print("ERRORR:VALUE is already exist!!")
            return
    def find_value(self,value):    #self sınıfın kendisi temsil eder.
        current_node = self.root
        while current_node is not Node:
            if current_node.value == value:
                return current_node.text
            if value<current_node.value:
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            elif value>current_node.value:
                if current_node.right is None:
                    return "ERROR : Not found"
                current_node = current_node.right
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
        return 1 + max(self._height(current_node.left),self._height(current_node.right))
    

if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet",32)
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Emirhan",31)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Burdur",15)
    my_tree.add_node("Konya",42)
    my_tree.add_node("Bilecik",11)

    print(my_tree.find_value(41))
    print(my_tree.find_value(82))
    print(my_tree.size())
    print(my_tree.height())


class Node:
    def __init__(self, text, value):
        self.text = text
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, text: str, value: int):
        self.root = Node(text, value)

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




            




