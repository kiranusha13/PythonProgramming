'''Strings are Immutable:
1. Once we try to modify it, if we try to modify the string it will create new string.

2.If new String doesn't have any new reference variable then it will be removed.

3.Python Internally uses string Interning.

4.String Interning is a process of checking string Intern Pool before creating 
any new Object.

Whenever we want to create a new object , Python first will check string intern pool, whether
that object already exist or not.

When object already exists in string Intern records then address of existing object will be reused.
'''
s1 = 'Kod'
s1 = s1.upper()
print(s1)

'''By using id() we can actually check the address'''
s2='K'
print(s2, id(s2))

s3 = 'Hello'
s4 = 'World'

print(s3, id(s3))
print(s4, id(s4))

print(s3[0])
print(s3[-1])

print('s3 Id of H:',id(s3[0]))
print('s4 Id of W:',id(s4[0]))

print('s3 Id of O:',id(s3[-1]))
print('s4 Id of O:',id(s4[2]))

print('s3 Id of l:',id(s3[2]))
print('s4 Id of l:',id(s4[3]))
print('s4 Id of l:',id(s4[3]))

