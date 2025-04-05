class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.__insert_rec(self.root, key)

    def __inorder_rec(self, node, result):
        if node:
            self.__inorder_rec(node.left, result)
            result.append(node.value)
            self.__inorder_rec(node.right, result)


    def inorder_traversel(self):
        result = []
        self.__inorder_rec(self.root, result)
        return result

    def __insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self.__insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.__insert_rec(node.right, key)
    def search(self, key):
        return self.__search(self.root, key)
    
    def __search(self, node, key):
        if node is None:
            return False
        if node.value == key:
            return True
        elif key < node.value:
            return self.__search(node.left, key)
        else:
            return self.__search(node.right, key)
    def is_empty(self): return self.root is None
    def find_min(self):
        if self.is_empty():return None
        return self.__find_min(self.root)
    def __find_min(self,node):
        while node.left:
            node = node.left
        return node.value
    def find_max(self):
        if self.is_empty():return None
        return self.__find_max(self.root)
    def __find_max(self,node):
        while node.right:
            node = node.right
        return node.value

    



bt = BinaryTree()
elements = [24, 20, 13, 50, 3, 32, 6]
for el in elements:
    bt.insert(el)




print(bt.inorder_traversel()[-1])
print(bt.inorder_traversel()[0])
print(bt.find_max())
print(bt.find_min())