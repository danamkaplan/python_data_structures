#!/usr/bin/python

class Node:
    """
    The building block of all the 
    data structures I will build
    """
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        print "%s" % (self.data)
    def get_data(self):
        return self.data

    def set_pointer(self, pointed_node):
        self.pointer = pointed_node

    def get_pointer(self):
        return self.pointer

class LinkedList:
    """
    """
    def __init__(self):
        self.head = None
        self.tail = None
        # init

    def insert(self, obj):
        # inserts a new node into the list
        new_node = Node(obj)
        self.tail = new_node
        if self.head == None:
            # make new node the head
            self.head = new_node
            self.tail = new_node
        else:
            # older tail to this new node
            self.tail.set_pointer(new_node)
            self.tail = new_node
            
    def size(self): 
        # returns size of list
        counter = 0
        return (counter)

    def search(self, obj): 
        # searches list for a node containing the requested data and returns that
        # node if found, otherwise raises an error
        end
    def delete(self, obj): 
        # searches list for a node containing the requested data and removes it
        # from list if found, otherwise raises an error
        end
    def print_list(self):
        current_node = self.head
        while current_node.get_data != self.tail.get_data:
            print current_node
            current_node = self.head.get_pointer
