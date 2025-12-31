# Linked List Implementation in Python
from xml.dom.minidom import Node

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print()

    def addatb(self, data):
        new = node(data)
        new.next = self.head
        self.head = new

    def addate(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def addatpos(self, pos, data):
        new = node(data)
        if pos == 0:
            new.next = self.head
            self.head = new
        else:
            temp = self.head
            for _ in range(pos - 1):
                if temp is None:
                    return
                temp = temp.next
            new.next = temp.next
            temp.next = new

    def deleteatb(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head = self.head.next

    def deleteate(self):
        if self.head is None:
            print("list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def deleteatpos(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(pos - 1):
                if temp.next is None:
                    return
                temp = temp.next
            temp.next = temp.next.next

    def searchnode(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("node found")
                return
            temp = temp.next
        print("node not found")

    def reverselist(self,n1):
            prev=None
            curr=n1
            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        


# --------- Testing ---------
s = LinkedList()

n1 = node(10)
s.head = n1
n2 = node(20)
n1.next = n2
n3 = node(30)
n2.next = n3
n4 = node(40)
n3.next = n4
n5 = node(50)
n4.next = n5

s.display()
s.searchnode(30)

print("after deleting a node at beginning")
s.deleteatb()
s.display()

print("after deleting a node at end")
s.deleteate()
s.display()

print("after deleting a node at position")
s.deleteatpos(2)
s.display()

print("after reversing thelinked list")
s.head=s.reverselist(n1)
s.display()
