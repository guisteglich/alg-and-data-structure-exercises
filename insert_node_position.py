'''
Given the pointer to the head node of a linked list and an integer to insert at a certain position, 
create a new node with the given integer as its data attribute, 
insert this node at the desired position and return the head
'''

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if llist == None:
        print("The linked list is empty")
        llist = new_node
        new_node.next = None
        return llist
    else:
        current = llist
        while position > 1:
            current = current.next
            position -=1
        aux = current.next
        current.next = new_node
        new_node.next = aux
        return llist
