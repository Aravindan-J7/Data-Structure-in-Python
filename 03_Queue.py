#Queue

'''
    queue is the linear data type which stores the values as First in First Out(FIFO)
'''

def queue(arr):
    
    for element in arr:
        print(element,end = " ")
    pass 

arr = list(map(int,input().split()))
queue(arr)