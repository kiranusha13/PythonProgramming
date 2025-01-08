'''Strings are Immutable:
1. Once we try to modify it, if we try to modify the string it will create new string.

2.If new String doesn't have any new reference variable then it will be removed
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
