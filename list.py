'''
1.In list we can store homogenousas well as heterogeneous data.
2.In list we can store duplicate values.
3.List  is an ordered collection of data: order of insertion will remain as it is in the output
4.lists are mutable .Once we declare the list we can modify it.
'''

li1 = [1,2,3,'usha',True]
print(li1,type(li1))

li1.append(300)
print(li1)

li1.insert(1,15)
print(li1)


#remove the first occurence
li1.remove(2)

#true or false
print(2 in li1)
print('kod' in li1)


#removed and return the last element
removed_ele = li1.pop()
print(removed_ele)
print(li1)

rem = li1.pop(4)
print(rem)
print(li1)

#del 
del li1[1]
print(li1)

#del li1
# print(li1)



