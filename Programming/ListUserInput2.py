li = input('Enter space sepearated elements')
print(li,type(li))
li = li.split()
print(li)
li = list(map,(int,li))
print(li)
print('K o d'.split())

tup = map(int,input("enter space sepearated elements").split())
print(tup)

li = map(int,input('Enter the input: ').split())
print(i for i in li if i%2 == 0)
