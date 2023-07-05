'''
람다 함수
'''

def plus_one(x):
    return x+1
print(plus_one(2))


plus_two = lambda x: x+2 # plus_two는 함수가 아니라 변수의 이름 
print(plus_two(3))



a = [1, 2, 3]
print(list(map(plus_one, a)))

print(list(map(lambda x: x+1, a))

# 익명의 표현식을 내장함수의 인자로 사용할 때 편리함. 
