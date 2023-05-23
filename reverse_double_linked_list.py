class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node
    

def reverse(llist):
    if llist == None:
        return None
    curr = llist
    while curr != None:
        curr.prev, curr.next = curr.next, curr.prev
        if curr.prev == None:
            llist = curr
        curr = curr.prev
    
    return llist



dlinkedList = DoublyLinkedList()
dlinkedList.insert_node(1)
dlinkedList.insert_node(2)
dlinkedList.insert_node(3)
dlinkedList.insert_node(4)

print(reverse(dlinkedList.head))
