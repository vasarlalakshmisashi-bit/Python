x=3
y=45
print(x/y)

#y=int(input("enter the age"))
if y>=18:
    print("eligible")
    if y>=60:
        print("senior citizen")
    else:
        print("adult")
else:
    print("not eligible")

x=[2,3,4,5,6]
for i in range(len(x)):
    print(x[i])
    for j in range(5):
        print(j)
#generate all sequnce from 1 to 30 and print only even numbers
for number in range(1,30):
    if number%2==0:
        print(number,end=" ")
        number=number=1;
