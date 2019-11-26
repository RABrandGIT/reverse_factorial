import math
def reverse_factorial(x):
    y = x
    for i in range(2,x):
        y = y/i
        print(y)
        if math.factorial(y)  == x:
            print("found")
            return y
            break
        
value = int(input("Enter number: ",))
print(reverse_factorial(value))
print("end")

        
