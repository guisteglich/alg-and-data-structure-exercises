import math
import os
import random
import re
import sys

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

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