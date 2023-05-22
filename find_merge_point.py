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

def findMergeNode(head1, head2):
    curr1 = head1
    curr2 = head2
    while curr1 != None: 
        while curr2 != None:
            if curr1 == curr2:
                return curr2.data
            curr2 = curr2.next
        curr2 = head2
        curr1 = curr1.next

# def findMergeNode(head1, head2): # Works with
#     li = []
#     while head1:
#         li.append(head1) 
#         head1 = head1.next

#     while head2:
#         if head2 in li:
#             return head2.data
#         head2 = head2.next

l1 = SinglyLinkedList()
l1.insert_node(1)
l1.insert_node(2)
l1.insert_node(3)
l2 = SinglyLinkedList()
l2.insert_node(1)
l2.insert_node(3)

print(findMergeNode(l1.head, l2.head))
