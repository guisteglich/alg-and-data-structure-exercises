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
        
def mergeLists(head1, head2):
    if head1 == None or head2 == None:
        return
    else:
        llist = SinglyLinkedList()
        while head1 and head2:
            if head1.data < head2.data:
                llist.insert_node(head1.data)
                head1 =  head1.next
            else:
                llist.insert_node(head2.data)
                head2 = head2.next
        if head1:
            while head1:
                llist.insert_node(head1.data)
                head1 =  head1.next
        else:
            while head2:
                llist.insert_node(head2.data)
                head2 =  head2.next

    return llist.head