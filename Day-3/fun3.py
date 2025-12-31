# Create a student class with attributes name, hall ticket number and branch of the student and also define a function which displays the student information
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
 #for above students include two attributes marks in two subjects names and write addtiondal percentage method to calculate the percentage of marks obtained by the student with displaying subjects names also
class student:
    def __init__(self,name,htn,branch,sub1,sub2,marks1,marks2):
        self.name=name
        self.htn=htn
        self.branch=branch
        self.sub1=sub1
        self.sub2=sub2
        self.marks1=marks1
        self.marks2=marks2
    def display(self):
        print("name:",self.name)
        print("hall ticket number:",self.htn)
        print("branch:",self.branch)
        print("subject 1:",self.sub1,"marks:",self.marks1)
        print("subject 2:",self.sub2,"marks:",self.marks2)
    def percentage(self):
        total=self.marks1 + self.marks2
        percent=(total/2)%100
        print("percentage:",percent)
stud1=student("sashi","12345","CSE","maths","science",85,90)
stud1.display()
stud1.percentage()
stud2=student("ramu","67890","ECE","maths","science",75,80)
stud2.display()
stud2.percentage()