import math
def factorial(num):
    n = num
    factorial = 1
    while n > 1:
        n=n/factorial
        factorial += 1
    if n == 1:
        return factorial - 1
    else:
        return False
    


#value = int(input("Enter number: ",))
#print(factorial(value))

        
