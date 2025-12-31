#print all the factors of a given number using function
def factors(n):
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result
num=int(input("enter a number"))
print("factors of",num,"are:",factors(num))
#print give number is prime or not using function
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#print whether a number is prime or not
number=int(input("enter a number")) 
if is_prime(number):
    print(number,"is a prime number")
else:
    print(number,"is not a prime number")
        
