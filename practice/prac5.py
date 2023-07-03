'''
중첩 반복문(2중 for문)
'''
for i in range(5):
    print("i:", i, sep=" ", end=" ")
    for j in range(5):
        print("j:", j, sep=" ", end=" ")
    print()

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()


for i in range(5):
    for j in range(5-i): # i=0, 1, 2, 3, 4 일 때, (5-i)는 5, 4, 3, 2, 1
        print("*", end=" ") 
    print()
