#node contains data,left child and right child
#binary tree
class node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
class binarytree:
    def __init__(self):
        self.root=None
    def inorder(self,root):
        if root==None:
            return
        else:
            self.inorder(root.leftchild)
            print(root.data,end=",")
            self.inorder(root.rightchild)
    def preorder(self,root):
        if root:
            print(root.data,end=",")
            self.preorder(root.leftchild)
            self.preorder(root.rightchild)
            return root
    def postorder(self,root):
        if root:
            self.postorder(root.leftchild)
            self.postorder(root.rightchild)
            print(root.data,end=",")
            return root 
#automating
    def insertnode(self, data):
        newnode = node(data)
# If tree is empty
        if self.root is None:
            self.root = newnode
            return
# Level order insertion using queue
        queue = [self.root]
        while queue:
            temp = queue.pop(0)

            if temp.leftchild is None:
                temp.leftchild = newnode
                return
            else:
                queue.append(temp.leftchild)

            if temp.rightchild is None:
                temp.rightchild = newnode
                return
            else:
                queue.append(temp.rightchild)
b=binarytree()
b.insertnode(10)
b.insertnode(20)
b.insertnode(30)
b.insertnode(40)
#n1=node(10)
#b=binarytree()
#b.root=n1
#n2=node(20)
#b.root.leftchild=n2
#n3=node(30)
#b.root.rightchild=n3
#n4=node(40)
#b.root.leftchild.leftchild=n4
#print(b.root.data)
#print(b.root.leftchild.data)
#print(b.root.rightchild.data)
#print(b.root.leftchild.leftchild.data)
print("the inorder is:")
b.inorder(b.root)
print()
print("the preorder is:")
b.preorder(b.root)
print()
print("the postorder is:")
b.postorder(b.root)