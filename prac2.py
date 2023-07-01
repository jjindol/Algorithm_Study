a = input("숫자를 입력하세요: ")
print(a)

a, b = input("숫자를 입력하세요: ").split() #띄어쓰기, 2와 3 분리
print(a+b) # 두 숫자가 연결됨

a, b = input("숫자를 입력하세요: ").split()
a = int(a)
b = int(b)
print(a + b) # 형 변환


a, b = map(int, input("숫자를 입력하세요: ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b) # 나머지
print(a**b) # 거듭제곱


a = 4.3
b = 5
c = a + b
print(type(c)) # 실수형




        
