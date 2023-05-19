class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node
    
    def show_ll(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

def removeDuplicates(llist):
    if llist == None:
        return None
    son = llist.next
    dad = llist
    while dad.next != None:
        if dad.data == son.data:
            dad.next = son.next
            son = son.next
        else:
            dad = son
            son = son.next
    return llist


# 1 > 2 > 2 > 3 > 4 > Null

# 3 >>> 4 > 5 >> Null

single_ll = SinglyLinkedList()
single_ll.insert_node(3)
single_ll.insert_node(3)
single_ll.insert_node(3)
single_ll.insert_node(4)
single_ll.insert_node(5)
single_ll.insert_node(5)

removeDuplicates(single_ll.head)

single_ll.show_ll()

