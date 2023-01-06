#Linked List
'''
    Algorithm:
        1) create Node class.
        2) create Linked list Node.
        3) create object for the Linked list class & assign head Node value by using Linked list Node.
        4) create each node and assign value & link each node to the address of the next variable.
        5) create seperate function for print the linked list values.

'''



class Node:                             #create Node
    def __init__(self,val):
        self.val = val 
        self.nxt = None 

class Llist:                            #create Node for Linked list

    def __init__(self):
        self.head = None 

    def printf(self):                   #function for print linked list values                   
        tmp = self.head 
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.nxt


obj = Llist()
obj.head = Node("10")                   #Assign head Node Value
a = Node("20")
b = Node("30")
c = Node("40")

#link each node
obj.head.nxt = a 
a.nxt = b 
b.nxt = c 

obj.printf()                           #call to print the linked list assigned value    