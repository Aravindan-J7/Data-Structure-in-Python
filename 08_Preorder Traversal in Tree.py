#Preorder Traversal

'''
    Algorihtm:
    1)create Node and assign head node in constructor(__init__ method)
    2)create method for insert the element
    3)write traversal algorithm as (root -> left -> right) values
'''

class Node:

    def __init__(self,val):                                 #asign head value using constructor method
        self.value = val
        self.left = None 
        self.right = None
    
    def insertion(self,val):                                #insert each element by calling this function                                
        if self.value:
            if val < self.value:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insertion(val)
            
            elif val > self.value:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insertion(val)
        
        else:
            self.value = val
    
    def preOrderTraversal(self,root):                        #visit as root->left->right
        res = []
        if root:
            res.append(root.value)
            res += self.preOrderTraversal(root.left)
            res += self.preOrderTraversal(root.right)
        return res


root = Node(int(input("Enter the Head Node value:")))

for i in range(int(input("How many values need to insert:"))):
    root.insertion(int(input("Enter the value:")))

print(root.preOrderTraversal(root))