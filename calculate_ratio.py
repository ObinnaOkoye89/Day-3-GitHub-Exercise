import Calculator

# Allow the user to define two numbers a & b
a = int(input("First number for the ratio opertaion?"))
b = int(input("Second number to the ratio operation?"))

# Calculate the ratio by importing your function ratio
result = Calculator.Ratio(a,b)
print(result)
