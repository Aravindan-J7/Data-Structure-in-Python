#Stack

'''
    Stack is the linear data type which stores the values as First in Last out.
'''

def stack(arr):
    
    for elements in arr[::-1]:
        print(elements,end=" ")
    
    
arr = list(map(int,input().split()))            #enter the elements
stack(arr)