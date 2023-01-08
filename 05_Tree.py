#Tree

'''
    Tree is a non-linear data structure where all elements are arranged in different memory location.

    Algorithm
    1) Create Node and constructor value as root,left,right
    2) Create Tree Node for assign root node of the tree.
    3) Create N child nodes & connect each of them as left and right.

'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None 
    

obj = Tree()
obj.root = Node(1)
b = Node(2)
c = Node(3)
obj.root.left = b                   #connect to root's node left node(child)
obj.root.right = c                  #connect to root's node right node(child)
print(obj.root.val)
print(obj.root.left.val)
print(obj.root.right.val)