#write a  python recusevie function program to print febomacci series upto 10 numbers and also implement the same using iteration
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
print(fibonacci_recursive(10))  
def fibonacci_iterative(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
print(fibonacci_iterative(10))
#find sum of n natural numbers using recursion
def sum_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_natural_numbers(n - 1)
print(sum_natural_numbers(10))  
#create a class of carthat has attributs color,model and brand and write a function to display the information of the car
class Car:
    def __init__(self, color, model, brand):
        self.color = color
        self.model = model
        self.brand = brand
    def display_info(self):
        return f"Car Brand: {self.brand}, Model: {self.model}, Color: {self.color}"
my_car = Car("Red", "Model S", "Tesla")
print(my_car.display_info())

#write a python program to create a class of rectangle that has attributes length and breadth and also define a function to calculate area and perimeter of the rectangle
x=[10,20,30]
print(x[-1])














