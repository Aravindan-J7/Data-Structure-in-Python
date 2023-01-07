#Deque 

'''
    deque is nothing but insertion and deletion can be performed both end
'''

class deque:

    def __init__(self,arr) -> None:
        self.arr = arr

    def InsertAtFront(self):
        tmp = int(input("Enter the element to insert at front:"))
        self.arr.insert(0,tmp)
        print("After insert the element:",self.arr)  

    def InsertAtLast(self):
        tmp = int(input("Enter the element to insert at last position:"))
        self.arr.append(tmp)
        print(arr)

    def DeleteAtFront(self):
        self.arr.pop(0)
        print("After the delete element at front:",arr) 

    def DeleteAtLast(self):
        self.arr.pop()
        print("After the delete element at end:",arr)


arr = list(map(int,input().split()))
obj = deque(arr)
obj.InsertAtFront()
obj.InsertAtLast()
obj.DeleteAtFront()
obj.DeleteAtLast()
