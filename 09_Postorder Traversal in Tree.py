#Postorder Traversal

'''
    Algorihtm:
    1)create Node and assign head node in constructor(__init__ method)
    2)create method for insert the element
    3)write traversal algorithm as (left -> right -> root) values
'''

class Node:

    def __init__(self,val):                                         #assign head value using constructor method
        self.value = val
        self.left = None 
        self.right = None
    
    def insertion(self,val):                                        #insert each element by calling this function
        if self.value:
            if val < self.value:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insertion(val)
            
            elif val > self.value:                                  #visit as left -> right -> root
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insertion(val)
        
        else:
            self.value = val
    
    def postOrderTraversal(self,root):
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res += self.postOrderTraversal(root.right)
            res.append(root.value)
        return res


root = Node(int(input("Enter the Head Node value:")))

for i in range(int(input("How many values need to insert:"))):
    root.insertion(int(input("Enter the value:")))

print(root.postOrderTraversal(root))