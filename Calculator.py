a = int(input("What would you like your first number to be?"))
b = int(input("What would you like your second number to be?"))


def Addition(a, b):
    return a + b
    
    
def Subtraction(a, b):
    return a - b
    

def Multiplication(a, b):
    return a * b
    
   
def Division(a, b):
    return a / b
    
def Ratio(a,b): 
    return (a/c)*100

c = Addition(a,b)
d = Subtraction(a,b)
e = Multiplication(a,b)
f = Division(a,b)
g = Ratio(a,b)

print(f" {c} is the sum of {a} and {b}")
print(f"{d} is the subtraction of {b} from {a}")
print(f"{e} is the multiplication of {a} and {b}")
print(f" {f} is the division of {a} by {b}")
print(f"The ratio of {a} to {b} is {int(g)} percent")
