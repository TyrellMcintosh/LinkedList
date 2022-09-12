from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_all(self):
        current = self.head
        while current != None:
            print("Name: {} Age: {} Weight {}".format(current.data.name,current.data.age,current.data.weight))
            current = current.next
    
    def add_first(self,data):        
        if (self.head == None):
            self.tail = self.head
        add = Node(data)
        add.data = data
        add.next = self.head
        self.head = add

    def add_last(self,data):
        add = Node(data)
        add.data = data
        # No tail means empty list
        if (self.tail == None):
            self.tail = self.head = add
        else:
            self.tail.next = add
            self.tail = add
    
    def delete_last(self):
        # Do nothing if list is empty
        if (self.head == None):
            return None
        # Delete the only item in list
        if (self.head.next == None):
            self.head = None
            self.tail = None
        else:
            current = self.head
            # Loop until tail is found
            while (current.next.next != None):
                current = current.next
            # Set new tail and delete old tail
            self.tail = current
            current.next = None