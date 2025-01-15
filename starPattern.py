# print("*")

# n = 5
# print("*" * n)

rows = 4
cols = 5
for i in range(rows):
    for j in range(cols):
        print('*', end = '')
    print()

r = 5
c = 5 

for i in range(r):
    for j in range(i+1):
        print('*',end = '')
    print()

for i in range(r):
    for j in range(i,r):
        print('*', end = '')
    print()

for i in range(r):
    for j in range(i+1):
        print('*',end = '')
    print()

for i in range(r):
    for j in range(i,r-1):
        print('*', end = '')
    print()

row = 8
col = 8
for i in range(row):
    for j in range(i+1):
        print('*', end = '')
    for j in range(i,row-1):
        print('-', end = "")
    for j in range(i,row-1):
        print('-', end = "")
    for j in range(i+1):
        print('*', end = '')
    print()
for i in range(row):
    for j in range(i,row-1):
        print('*', end = "")
    for j in range(i+1):
        print(' ', end ="")
    for j in range(i+1):
        print(' ', end ="")
    for j in range(i,row-1):
        print('*', end = "")
    print()
