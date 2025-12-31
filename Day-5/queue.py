#queue using list
class queue:
    def __init__(self,size):
        self.queue=[]
        self.size=size
    def enqueue(self,data):
        if self.is_full():
            print("queue is full,elements can not be inserted") 
        else:
            self.queue.append(data)
    def deque(self):
        if self.is_empty():
            print("queue is empty") 
        else:
            self.queue.pop(0) #delete element of indexes  
    def is_full(self):
        return len(self.queue)==self.size
    def is_empty(self):
        return len(self.queue)==0
    def peek(self):
        return self.queue[0] #front element
    def displayq(self):
        for element in self.queue:
            print(element)
q=queue(5)  
q.enqueue(10) 
q.enqueue(20) 
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.displayq()
print()
print(q.is_full())
print("the front element of the queue is",q.peek())
print("after deleting elments from queue")
q.deque()
q.displayq()
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
print(q.is_empty())
print(q.is_full())
#queue using linkedlist(no is_full and size operations)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        newnode=node(data)
        if self.front==None:
            self.front=newnode
            self.rear=newnode  
        else:
            self.rear.next=newnode
            self.rear=self.rear.next#(newnode)  
    def deque(self):
        if self.front==None:
            print("queue is empty")  
            return None
        else:
            removed=self.front.data  #(deleted element need to be printed it is stored using removed)
            self.front=self.front.next
            return removed
    def is_empty(self):
        return self.front==None

    def peek(self):
        if self.is_empty():
            print("queue is emoty")
        else:
            print("the frint element is:",self.front.data)    
    def displayq(self):
        if self.is_empty():
            print("the queue is empty")
        else:
            temp=self.front
            while temp:
                print(temp.data,end="-->") 
                temp=temp.next   
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.displayq()
print()
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
q.displayq()
print()
print(q.is_empty())


#classsification of queues
#double ended queue-delete or enter elements on bothends 
#priority queue-element which has highest priority deleted first
#circular queue-no wastage of memory(feedback connection from last node to first node)



#double ended queue
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doubleendedque():
    def __init__(self):
        self.front=None
        self.rear=None
    def eneque(self,data):
        newnode=node(data)
        if self.front is None:
            self.front=newnode
            self.rear=newnode
        else:
            temp=self.front
            self.front.prev=newnode
            self.front=newnode
            newnode.next=temp

    def dequeue(self):
        if self.front is None:
            print("queue is empty")
            return None
        else:
            removed=self.rear.data
            self.rear=self.rear.prev
            self.rear.next=None
            return removed
              
    def is_empty(self):
        return self.front==None
    def peek(self):
        return self.front.data
    #def displaydeque(self):
        #if self.front is None:
            #print("the deque is empty")
        #else:
            #temp=self.front
            #while temp:
                #print(temp.data,end="-->")
                #temp=temp.next
dq=doubleendedque()
dq.eneque(10)+
dq.eneque(20)
dq.eneque(30)
dq.eneque(40)
dq.eneque(50)
dq.displaydeque()
dq.dequeue()
print("after deleting elemnt from deque")
dq.displaydeque()
print("the front elmeent of deque is",dq.peek())
print(dq.is_empty())

            






                             





        








































