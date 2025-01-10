#If string is holding integre then it can be converted into int
a = '30'
b = int(a)
print(a, type(a))
print(b, type(b))

# str to integer conversion is not allowed
x='Kod'
print(x, type(x))
# y = int(x)
# print(y, type(y))

# p = float(input('Enter float type data'))
# print(p,type(p))

#bool() if any non-zero value or empty string then it is false otherwise true(for any string , any value except 0)
q = 12
q = bool(q)
print(q,type(q))

print(bool('Kodnest'))
print(int('11'))
print(float('22.22'))
print(bool(''))
print(bool(0))
print(bool(10))
# print(int('12.56'))#error. String of float not convert into int
print(int(12.56))

# taking float value from user and converting it into int
value = int(float(input('Enter price: FLOAT VALUE')))
print(value, type(value))