'''
리스트와 내장함수
'''

import random as r
a=[]
print(a)
b=list()
print(b)

a=[1, 2, 3, 4, 5]
print(a)
print(a[0])

b=list(range(1, 11))
print(b)

c=a+b
print(c) # 두 리스트를 합친다.

print(a)
a.append(6) # 리스트에 값을 추가 
print(a)

a.insert(3, 7) # 3번 인덱스에 7이라는 값이 들어간다.
print(a) # [1, 2, 3, 7, 4, 5, 6]

a.pop() # 맨 뒤 원소 삭제
print(a)
a.pop(3) # n번 인덱스의 값 삭제 
print(a)

a.remove(4)
print(a) # 4에 해당하는 값을 찾아서 삭제 


print(a.index(5)) # 인덱스의 5 값이 몇번 인덱스에 있나?

a = list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))

r.shuffle(a) # r은 랜덤값
print(a)
a.sort()
print(a) # 다시 오름차순으로
a.sort(reverse=True)
print(a) # 내림차순으로 정렬
a.clear()
print(a)




















