class Node:
    def _init_(self, data,):
        self.data = data
        self.next = None
class cll:
    def _init_(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        print(temp.data,end="-->")
        temp=temp.next
        while temp!=self.head:
            print(temp.data,end="-->")
            temp=temp.next            
        
c=cll()  
n1=Node(10)
c.head=n1
c.tail=n1
n1.next=n1
n2=Node(20)
c.tail=n2
n1.next=n2
n2.next=n1
n3=Node(30)
c.tail=n3
n2.next=n3
n3.next=n1
n4=Node(40)
c.tail=n4
n3.next=n4
n4.next=n1
c.display()