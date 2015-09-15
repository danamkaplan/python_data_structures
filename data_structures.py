#!/usr/bin/python

class Node(object):
    """
    The building block of all the 
    data structures I will build
    """
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer
    def __repr__(self):
        print "%s" % (self.data)
    def get_data(self):
        return self.data

    def set_pointer(self, pointed_node):
        self.pointer = pointed_node

    def get_pointer(self):
        return self.pointer

class LinkedList(object):
    """
    """
    def __init__(self):
        self.head = None
        self.tail = None
        # init

    def insert(self, obj):
        # inserts a new node into the list
        new_node = Node(obj)        
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
        counter = 1
        if self.head == None:
            counter = 0
        current_node = self.head
        while current_node != self.tail:
            counter = counter + 1
            current_node = current_node.get_pointer()
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
        while current_node != self.tail:
            print current_node.get_data()
            current_node = current_node.get_pointer()

class Stack(LinkedList):
    def __init__(self):
        end
    def push(obj):
        end
    def pop():
        return(obj)

''' not quite ready
class Queue(LinkedList):
    def __init__(self):
        end
    def 
'''
