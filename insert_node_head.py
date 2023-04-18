'''
Given a pointer to the head of a linked list, insert a new node before the head. 
The next value in the new node should point to head and the data value should be replaced
with a given value. Return a reference to the new head of the list. 
The head pointer given may be null meaning that the initial list is empty.
'''

def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    
    if llist == None:
        print("The linked list is empty")
        llist = new_node
        llist.next = None
        return new_node
    else:
        aux = llist
        llist = new_node
        new_node.next = aux
        return new_node