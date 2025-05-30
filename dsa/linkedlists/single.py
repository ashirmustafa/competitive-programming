# Node class aik element ko represent karta hai linked list mein
from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data  # value store karta hai
        self.next: Optional['Node'] = None  # next node ki taraf point karta hai, shuru mein None


# LinkedList class poori list ko manage karta hai
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # list shuru mein khaali hoti hai

    # Add a new node at the end of the list
    # List ke end par naya node add karta hai
    def append(self, data):
        new_node = Node(data)  # naya node banata hai
        if self.head is None:  # agar list khaali hai to naya node head ban jata hai
            self.head = new_node
        else:
            current = self.head
            while current.next:  # last node tak jata hai
                current = current.next
            current.next = new_node  # last node ko naye node se jor deta hai

    # Print all elements in the list
    # List ke tamam elements print karta hai
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # har node ka data print karta hai
            current = current.next
        print("None")  # list ka end show karta hai

# Example usage:
# List banata hai aur usme kuch values add karta hai
my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.print_list()