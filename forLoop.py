
'''for control_variable in iterable_object'''

for i in 'Kodnest':
    print(i)

for j in [10,20,30]:
    print(j)

for i in range(1,11):
    print(i)

for i in range(11,21,2):
    print(i, end = " ")

#start value 0 by default if not mentioned
for i in range(5):
    print(i,end=" ")
print(" ")
#WAP to print all even numbers from 1-10:
for i in range(0,11,2):
    print(i, end = " ")

i=0
while (i < 10):
    print(i+100)
    i = i+1

#WAP to pritn numbers from 1-10 if num is 6 then skip printing 
for i in range(1,10):
    if(i == 6):
        continue
    print(i)

for i in range(1,10):
    if(i == 5):
        break
    print(i)