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


def compare_lists(llist1, llist2):
    if llist1.data != llist2.data:
        return 0
    else:
        if llist1.next == None or llist2.next == None:
            return 0
        else:
            current1 = llist1
            current2 = llist2
            while current1.next.data == current2.next.data:
                current1 = current1.next
                current2 = current2.next
                if current1.next == None and current2.next == None:
                    ok = True
                    break
                elif current1.next == None or current2.next == None:
                    ok = False
                
            if ok:
                return 1
            else:
                return 0
            
def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    if llist1 or llist2:
        return 0
    return 1
            
llist1 = SinglyLinkedList()
llist2 = SinglyLinkedList()

llist1.insert_node(1)
llist1.insert_node(2)

llist2.insert_node(1)

print(compare_lists(llist1, llist2))


llist12 = SinglyLinkedList()
llist22 = SinglyLinkedList()

llist12.insert_node(1)
llist12.insert_node(2)

llist22.insert_node(1)
llist22.insert_node(2)

print(compare_lists(llist12, llist22))