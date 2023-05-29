class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self): 
        self.root = None
            
    def insert(self, val):
        node = Node(val)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while current:
                dad = current
                # left
                if current.info > val:
                    current = current.left
                    if current == None:
                        dad.left = node
                        return
                else:
                    current = current.right
                    if current == None:
                        dad.right = node
                        return 