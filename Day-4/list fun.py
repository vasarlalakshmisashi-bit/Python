#list comprehension to get squares of the given list
x=[2,4,3]
squares=[i**2 for i in x]
print(squares)
#multiples of 3 in given numbers
x=[5,2,1]
multiples_of_3=[i for i in x if i%3==0]
print(multiples_of_3)
#dictionary comprehension to get square of numbers of its keys
dict={1:2,3:4,5:6}
squared_dict={k:v**2 for k,v in dict.items()}
print(squared_dict)
#generate a dictionary with numbers and their squares
result={i:i*i for i in range(1,6)}
print(result)