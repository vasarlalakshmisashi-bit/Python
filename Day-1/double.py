#Implement double linked list with previous and next as address fields and with 1 data feeding
class Node:
    def __init__(self, data,):
        self.data = data
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    #displaying the nodes  
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next
    def addat_beginning(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head.prev=new
            self.head=new   
    def addat_end(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp
    def addatposition(self,pos, data):
        new=Node(data)
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        new.next=temp.next
        if temp.next: #if statement can be used only if needed
            temp.next.prev=new 
        temp.next=new
        new.prev=temp
    def deleteat_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None  
    def deleteat_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def deleteat_position(self,pos):
        temp=self.head #temp means the node next to deleting node
        current=self.head.next #current means the node which is to be deleted
        for i in range(pos-2):
            temp=temp.next 
            current=current.next
        temp.next=current.next
        current.next.prev=temp
    def search(self,data):
        temp=self.head 
        flag=0
        while temp: #when temp.next is given it will not check the last node
            if temp.data==data:
                flag=1
                break
                #print("node is found")--->this line is used when there is no flag variable
            temp=temp.next
        #print("node is not found")
        if flag==1:
            print("node is found")
        else:
            print("node is not found")  
    def reversedll(self):
        temp=self.tail
        while temp:
            print(temp.data,end="<-->")  
            temp=temp.prev          
           
d=dll()
#creating nodes dynamically using loop
listofnodes=[10,20,30,40,50]
n1=Node(listofnodes[0])
d.head=n1
d.tail=n1
prevnode=n1
for i in range(1,len(listofnodes)):
    nextnode=Node(listofnodes[i])
    prevnode.next=nextnode
    nextnode.prev=prevnode
    d.tail=nextnode
    prevnode=nextnode
#n1=Node(10) this is manual type creation of nodes
#d.head=n1
#n2=Node(20)
#n1.next=n2
#n2.prev=n1
#n3=Node(30)
#n2.next=n3
#n3.prev=n2
#n4=Node(40)
#n3.next=n4
#n4.prev=n3
#n5=Node(50)
#n4.next=n5
#n5.prev=n4
d.display()
print()
print("adding the node at the beginning")
d.addat_beginning(5)
d.display()
print()
print("adding the node at the end")
d.addat_end(60)
d.display()
print()
print("adding node at the given position")
d.addatposition(4,45)
d.display()
print()
print("after removing the node at the beginning")
d.deleteat_beginning()
d.display() 
print()
print("after removing the node at the end")
d.deleteat_end()
d.display()
print()
print("after deleting the node the given position")
d.deleteat_position(5)
d.display()
d.search(35)
print("after reversal traversal of dll")
d.reversedll()