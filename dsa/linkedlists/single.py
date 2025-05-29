# Node class - represents one element in the linked list
from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data  # store the value
        self.next: Optional['Node'] = None  # points to the next node, initially None

# LinkedList class - manages the whole list
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # start with empty list

    # Add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # create new node
        if self.head is None:  # if list is empty, new node is head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # move to the last node
                current = current.next
            current.next = new_node  # link last node to new node

    # Print all elements in the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # end of list

# Example usage:
my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.print_list()
