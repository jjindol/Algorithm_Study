'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]
print(a[:3]) # 0, 1, 2 인덱스 출력
print(a[1:4])
print(len(a)) # 리스트의 길이 출력

for i in range(len(a)):
    print(a[i], end=" ")
print()

for x in a:
    if x%2==1:
        print(x, end=" ")
print()

for x in enumerate(a):
    print(x)
    

print("-------------")

b=(1, 2, 3, 4, 5)
print(b[0])
# b[0]=7
# tuple은 다른 데이터 타입의 요소를 담을 수 있으며, 한 번 생성되면 변경할 수 없다.


for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(x<60 for x in a): # 모두 만족시키면 True 
    print("True")
else:
    print("False")
print()

if any(x<30 for x in a): # 한번이라도 만족시키면 True
    print("True")
else:
    print("False")
print()



