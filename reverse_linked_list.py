'''
Given the pointer to the head node of a linked list, change the next pointers of the nodes 
so that their order is reversed. 
The head pointer given may be null meaning that the initial list is empty.
'''

def reverse(llist):
    if llist == None:
        print("The linked list is empty")
        return llist
    else:
        current = llist
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        llist = previous
        return llist