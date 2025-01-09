# Input method always takes an input as a string
a = input('Enter the number')
print(a,'DataType of num1 is',type(a))

b = int(input('Enter the number'))
print(b,'DataType of num1 is',type(a))

num1 = int(input('Enter the num1'))
num2 = int(input('Enter the num2'))

print(f'Addition of {num1} and {num2} is {num1+num2}')
print(f'Subtraction of {num1} and {num2} is {num1-num2}')
print(f'Multiplication of {num1} and {num2} is {num1 * num2}')
print(f'Division of {num1} and {num2} is {num1/num2}')