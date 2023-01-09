#Tree - insert elements

'''
    Algorithm:
    1)create Node
    2)assign head value
    3)write code for insertion that means if element is less than to head node that need to assign at left or if element
      is greater than head node it need to assign right side of the head node.
'''

class Node:
    
    def __init__(self,val):                         #create constructor to set head value
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val):                                               
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def printTree(self):                            #print function that prints the inserted element in tree 

        if self.left:
            self.left.printTree()
        print(self.val)

        if self.right:
            self.right.printTree()
        


obj = Node(int(input("Enter the head Node:")))
for i in range(int(input("How many values to be inserted in tree:"))):
    obj.insert(int(input()))
obj.printTree()
