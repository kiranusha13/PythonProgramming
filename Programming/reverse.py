li = [15,20,30,7]
print("before reverse: ",li)
li.reverse()
print('After reverse:',li)

li2 = [11,12,13]
reverse_li2 = list(reversed(li2))
print(li2)
print(reverse_li2)

li3 = [1,5,2,9]
new_reverse_li3 = list(reversed(li3)) # creating new reverse list
print(new_reverse_li3)
li3.reverse() #=== reversing original list
print(li3)