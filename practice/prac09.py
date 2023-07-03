'''
2차원 리스트 생성과 접근
'''

a=[[0]*3 for _ in range(3)]
print(a)
a[0][1]=1
a[1][1]=2
print(a)

for x in a: # x가 0, 1, 2행 순서로 출력됨
    print(x)
print()

for x in a:
    for y in x:
        print(y, end=" ")
    print()

'''
1. a는 2차원 리스트이며, 첫 번째 for 루프의 반복 변수 x는 a의 각 행을 나타낸다.
2. 두 번째 for 루프의 반복 변수 y는 x의 각 요소를 나타낸다.
3. print(y, end=" ")는 y를 출력하고 공백으로 구분하여 한 줄로 출력한다.
4. 내부 for 루프가 종료되면 print()를 사용하여 줄바꿈을 수행한다.
'''
