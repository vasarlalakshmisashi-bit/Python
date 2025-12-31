#stack using list
x=[10,20,30]
print(x[-1])

#stack ussing array and oops
class Stack:
    def _init_(self,size):
        self.stack=[]
        self.size=size
    def push(self,data):
        if self.is_full():
            print("stack is full")
        else:
            self.stack.append(data)
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            x=self.stack.pop()
            print("the deleted element is:",x)
            return None
    def is_empty(self):
        return len(self.stack)==0  
    def sizeofstack(self):
        return len(self.stack)
    def displaystack(self): 
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack[-1]
    def is_full(self):
        return len(self.stack)==self.size
    
st=Stack(4)
st.push(10)
st.push(20)
st.push(30)
st.push(40)
#st.pop()  
#st.pop()
print(st.is_empty())
#print(st.sizeofstack()) 
#print(st.stack)
st.push(50)
st.push(60)
st.displaystack()
#print(st.peek())


#stack using array and without oops
stack=[]
size=5
def push(data):
    if is_full():
        print("stack is full")
    else:
        stack.append(data)
def pop():
    if is_empty():
        return "stack is empty"
    else:
        x=stack.pop()
        print("the deleted element is:",x)
        return None
def is_empty():
    return len(stack)==0  
def sizeofstack():
    return len(stack)
def displaystack(): 
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
def peek():
    if is_empty():
        return "stack is empty"
    else:
        return stack[-1]
def is_full():
    return len(stack)==size
push(10)
push(20)
push(30)
push(40)
#pop()  
#pop()
#print(is_empty())
#print(sizeofstack()) 
#print(stack)
push(50)
push(60)
displaystack()
#print(st.peek())
