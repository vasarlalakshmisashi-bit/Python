class computer:
    def __init__(self, cpu, ram, hdd):
        self.cpu=cpu
        self.ram=ram    
        self.hdd=hdd
com1=computer("i7", "8gb", "512gb")
com2=computer("i5", "16gb", "1tb")
print(com1.cpu)
print(com1.ram)
print(com1.hdd)
class computer:
    def __init__(self, cpu, ram, hdd):
        self.cpu=cpu
        self.ram=ram    
        self.hdd=hdd
com1=computer("i7", "8gb", "512gb")
com2=computer("i5", "16gb", "1tb")
com1.cpu="i9"
print(com1.cpu)
print(com1.ram)
print(com1.hdd)
#oops concepts using functions
class computer:
    def __init__(self, cpu, ram, hdd):
        self.cpu=cpu
        self.ram=ram    
        self.hdd=hdd
    def display(self):
        com1=computer("i7", "8gb", "512gb")
        com2.display()     
#create a student class with attributes name, hall ticket number and branch of the student and also define a functionwhich displays the student information
class student:
    def __init__(self,name,htn,branch):
        self.name=name
        self.htn=htn
        self.branch=branch
        def display(self):
            print("name:",self.name)
            print("hall ticket number:",self.htn)
            print("branch:",self.branch)
stud1=student("sashi","12345","CSE")
stud1.display()
stud2=student("ramu","67890","ECE")
stud2.display()
#create a student class with attributes name, hall ticket number and branch of the student and also define a functi
class student:
    def __init__(self,name,htn,branch):
        self.name=name
        self.htn=htn
        self.branch=branch
        def display(self):
            print("name:",self.name)
            print("hall ticket number:",self.htn)
            print("branch:",self.branch)
stud1=student("sashi","12345","CSE")
stud2=student("ramu","67890","ECE")
stud1.display()
stud2.display() 
