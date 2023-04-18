
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


'''
You are given the pointer to the head node of a linked list and an integer to add to the list. 
Create a new node with the given integer. Insert this node at the tail of the linked list and return 
the head node of the linked list formed after inserting this new node. 
The given head pointer may be null, meaning that the initial list is empty.
'''
def insertNodeAtTail(head, data):
    novo_node = SinglyLinkedListNode(data)
    if head == None:
        head = novo_node
        novo_node.next = None
    else:
        atual = head
        while atual.next != None:
            atual = atual.next
        atual.next = novo_node
        novo_node.next = None
    return head