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


def sortedInsert(llist, data):
    curr = llist
    node = DoublyLinkedListNode(data)

    if data < llist.data:
        node.next = llist
        llist.prv = node
        return node
    
    while curr.next is not None and curr.next.data <= data:
        curr = curr.next

    node.next = curr.next
    if curr.next is not None:
        curr.next.prev = node
    curr.next = node
    node.prev = curr


    return llist

dll = DoublyLinkedList()
dll.insert_node(1)
dll.insert_node(3)
dll.insert_node(4)
dll.insert_node(10)

# dll.insert_node(1)
# dll.insert_node(2)
# dll.insert_node(3)

print(sortedInsert(dll.head, 5))