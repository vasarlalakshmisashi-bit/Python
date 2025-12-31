#python function to find sum of n natural numbers
def sum_natural_numbers(n):
    if n<=0:
        return 0
    else:
        return n + sum_natural_numbers(n-1)
#example usage
result = sum_natural_numbers(10)
print("Sum of first 10 natural numbers is:", result)

