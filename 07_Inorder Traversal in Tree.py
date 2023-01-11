#Inorder Traversal

'''
    Algorihtm:
    1)create Node and assign head node in constructor(__init__ method)
    2)create method for insert the element
    3)write traversal algorithm as (left -> root -> right) values
'''


class Node:

    def __init__(self,val):                                     #assign head value using constructor method
        self.value = val
        self.left =  None
        self.right = None
    
    def insertion(self,val):                                    #insert each element by calling this function
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

    def inorderTraversal(self,root):                            #visit as left -> root -> right
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.value)
            res += self.inorderTraversal(root.right)
        return res

root = Node(int(input("Enter the Head Node value:")))

for i in range(int(input("How many values need to insert:"))):
    root.insertion(int(input("Enter the value:")))

print(root.inorderTraversal(root))